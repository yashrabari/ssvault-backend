from atexit import register
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from users.forms import UserChangeForm, UserCreationForm
from users import models

User = get_user_model()

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "phone_number", "is_2FA", "verification_period", "storage", "storage_left", "subscription_name"]
    search_fields = ["name", "email"]

admin.site.register(models.PasswordReset)
admin.site.register(models.TwoFactorAuthentication)
admin.site.register(models.EmailTokenVerification)
admin.site.register(models.Category)
admin.site.register(models.Buddy)
admin.site.register(models.BuddyInvitation)