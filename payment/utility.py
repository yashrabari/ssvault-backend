from raspy_art_33412.settings import STRIPE_TEST_SECRET_KEY

import stripe
import djstripe

stripe.api_key = STRIPE_TEST_SECRET_KEY


def get_customer(user):
    if user.customer_account:
        customer_id = user.customer_account.id
    else:
        customers_data = stripe.Customer.list().data
        customer = None
        for customer_data in customers_data:
            if customer_data.email == user.email:
                customer = customer_data
                break
        if customer is None:
            customer = stripe.Customer.create(email=user.email)
        djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
        user.customer_account = djstripe_customer
        user.save()
        customer_id = djstripe_customer.id
    return user, customer_id
