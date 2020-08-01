from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.conf import settings

from stripe import Customer

from .models import BillingProfile

User = settings.AUTH_USER_MODEL


@receiver(pre_save, sender=BillingProfile)
def billing_profile_created_receiver(sender, instance, *args, **kwargs):
    if not instance.customer_id and instance.email:
        # print("ACTUAL API REQUEST Send to Stripe")
        customer = Customer.create(
            email=instance.email
        )
        # print(customer)
        instance.customer_id = customer.id


@receiver(post_save, sender=User)
def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)


