from django.db import transaction

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import SubscriptionSetupSerializer
from .models import SubscriptionSetup
from .utility import get_customer
from raspy_art_33412.settings import STRIPE_TEST_SECRET_KEY

import stripe
import djstripe

stripe.api_key = STRIPE_TEST_SECRET_KEY


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSetupSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    queryset = SubscriptionSetup.objects.all()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_cards(self, request):
        user, customer_id = get_customer(request.user)
        payment_methods = stripe.PaymentMethod.list(customer=customer_id, type='card')
        return Response(payment_methods)

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def revoke_payment_method(self, request):
        payment_method_id = request.data.get('payment_method', None)
        if payment_method_id is None:
            return Response({'detail': 'Missing Payment Method ID'}, status=status.HTTP_400_BAD_REQUEST)
        user, customer_id = get_customer(request.user)
        payment_method = stripe.PaymentMethod.detach(payment_method_id)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method)
        payment_methods = stripe.PaymentMethod.list(customer=customer_id, type='card')
        return Response(payment_methods)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def add_payment_method(self, request):
        payment_method_id = request.data.get('payment_method', None)
        if payment_method_id is None:
            return Response({'detail': 'Missing Payment Method ID'}, status=status.HTTP_400_BAD_REQUEST)
        user, customer_id = get_customer(request.user)
        payment_method = stripe.PaymentMethod.attach(payment_method_id, customer=customer_id)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method)
        payment_methods = stripe.PaymentMethod.list(customer=customer_id, type='card')
        return Response(payment_methods)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def set_default(self, request):
        payment_method_id = request.data.get('payment_method', None)
        if payment_method_id is None:
            return Response({'detail': 'Missing Payment Method ID'}, status=status.HTTP_400_BAD_REQUEST)
        user, customer_id = get_customer(request.user)
        
        last_default_pms = stripe.PaymentMethod.list(customer=customer_id, type='card')
        for method in last_default_pms:
            if method.metadata:
                stripe.PaymentMethod.modify(
                    method.id,
                    metadata={"default": False}
                )
        payment_method = stripe.PaymentMethod.modify(
            payment_method_id,
            metadata={"default": True})
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method)
        payment_methods = stripe.PaymentMethod.list(customer=customer_id, type='card')
        customer = stripe.Customer.modify(
            customer_id,
            invoice_settings = {
                "default_payment_method": payment_method_id,
            },
        )
        djstripe.models.Customer.sync_from_stripe_data(customer)
        return Response(payment_methods)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def test_payment_method(self, request):
        if request.data.get('decline', False):
            payment_method = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": "4000000000000002",
                    "exp_month": 2,
                    "exp_year": 2023,
                    "cvc": "314",
                },
                )
        else:
            payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 2,
                "exp_year": 2023,
                "cvc": "314",
            },
            )
        return Response(payment_method)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def plans(self, request):
        prices = stripe.Price.list(active=True, limit=100)
        for price in prices:
            djstripe.models.Price.sync_from_stripe_data(price)
        return Response(prices)

    @action(detail=False, methods=['patch'], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def swap_plan(self, request): 
        subscription = request.user.subscription
        items = request.data.get('items', None)
        sub = stripe.Subscription.modify(
            subscription.id,
            cancel_at_period_end=False,
            proration_behavior='create_prorations',
            items=items
        )
        djstripe.models.Subscription.sync_from_stripe_data(sub)
        return Response(sub, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def additional_plan(self, request):
        subscription = request.user.subscription
        if not subscription:
            return Response("User needs to already be subscribed to add an additional plan", status=status.HTTP_400_BAD_REQUEST)
        price = request.data.get('price_id')
        try:
            sub = stripe.SubscriptionItem.create(
                subscription=subscription.id,
                price=price
            )
        except stripe.error.InvalidRequestError as e:
            return Response("You cannot subscribe to a plan with a different billing interval", status=status.HTTP_400_BAD_REQUEST)
        djstripe.models.SubscriptionItem.sync_from_stripe_data(sub)
        return Response(sub)

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def unsubscribe_subscription(self, request): 
        subscription = request.user.subscription
        sub = stripe.Subscription.delete(subscription.id)
        djstripe.models.Subscription.sync_from_stripe_data(sub)
        return Response("You've successfully unsubscribed", status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def unsubscribe_plans(self, request): 
        items = request.data.get('items', None)
        for item in items:
            sub_item = stripe.SubscriptionItem.delete(item)
            djstripe.models.SubscriptionItem.sync_from_stripe_data(sub_item)
        return Response("You've successfully unsubscribed", status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    @transaction.atomic
    def subscribe(self, request):
        subscription = request.user.subscription
        if subscription and subscription.status != "canceled":
            return Response({'detail': 'User is already subscribed'}, status=status.HTTP_400_BAD_REQUEST)

        payment_method_id = request.data.get('payment_method', None)
        plan_ids = request.data.get('plan_ids', None)
        if payment_method_id is None:
            return Response({'detail': 'Missing Payment Method ID'}, status=status.HTTP_400_BAD_REQUEST)

        user, customer_id = get_customer(request.user)
        payment_method = stripe.PaymentMethod.retrieve(payment_method_id)

        coupon = request.data.get('coupon', None)
        try:
            if coupon:
                subscription = stripe.Subscription.create(
                    customer=customer_id,
                    default_payment_method=payment_method_id,
                    items=plan_ids,
                    expand=['latest_invoice.payment_intent'],
                    coupon=coupon
                )
            else:
                subscription = stripe.Subscription.create(
                    customer=customer_id,
                    default_payment_method=payment_method_id,
                    items=plan_ids,
                    expand=['latest_invoice.payment_intent']
                )
            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)
        except stripe.error.CardError as e:
            return Response({'detail': 'Card Declined'})

        # associate customer and subscription with the user
        request.user.subscription = djstripe_subscription
        request.user.save()

        return Response(subscription, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get', 'post', 'delete', 'patch'], permission_classes=[IsAdminUser])
    def coupons(self, request):
        if request.method == "GET":
            coupons = stripe.Coupon.list()
            for coupon in coupons:
                djstripe.models.Coupon.sync_from_stripe_data(coupon)
            return Response(coupons)
        elif request.method == "POST":
            amount = request.data.get('amount')
            name = request.data.get('name', 'no-name')
            duration = request.data.get('duration', 'forever')
            if duration != "once" and duration != "forever":
                return Response({"duration": "Invalid Entry"}, status=status.HTTP_400_BAD_REQUEST)
            coupon = stripe.Coupon.create(
                percent_off=int(amount),
                duration=duration,
                name=name
            )
            djstripe.models.Coupon.sync_from_stripe_data(coupon)
            return Response(coupon)
        elif request.method == "DELETE":
            coupon_id = request.data.get('coupon_id')
            coupon = stripe.Coupon.delete(coupon_id)
            return Response('Coupon deleted successfully')

    @action(detail=False, methods=['get', 'patch', 'delete', 'post'], permission_classes=[IsAdminUser])
    def admin_plans(self, request):
        if request.method == "GET":
            prices = stripe.Price.list(active=True, limit=100)
            for price in prices:
                djstripe.models.Price.sync_from_stripe_data(price)
            return Response(prices)
        elif request.method == "DELETE":
            price_id = request.data.get('plan_id')
            price = stripe.Price.modify(
                price_id,
                active=False
            )
            return Response("Plan deleted successfully")
        elif request.method == "POST":
            amount = int(request.data.get('amount'))
            interval = request.data.get('interval')
            nickname = request.data.get('nickname')
            description = request.data.get('description', '')
            product = request.data.get('product')
            price = stripe.Price.create(
                unit_amount=amount,
                currency="usd",
                recurring={
                    "interval": interval
                },
                product=product,
                nickname=nickname,
                metadata={'description': description}
            )
            prices = stripe.Price.list(active=True, limit=100)
            for price in prices:
                djstripe.models.Price.sync_from_stripe_data(price)
            return Response(prices)
