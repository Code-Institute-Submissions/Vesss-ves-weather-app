from decimal import Decimal

from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver

from .models import Cart


@receiver(m2m_changed, sender=Cart.products.through)
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
        instance.subtotal = total
        instance.save()


@receiver(pre_save, sender=Cart)
def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.08)  # 8% tax
    else:
        instance.total = 0

