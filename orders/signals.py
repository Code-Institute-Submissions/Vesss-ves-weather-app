from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Order
from cart.models import Cart
from weatherapp.utils import unique_order_id_generator


@receiver(pre_save, sender=Order)
def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        # set unique id for each order
        instance.order_id = unique_order_id_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)


@receiver(post_save, sender=Order)
def order_update_total_price(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()

