from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Donation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    scid = models.CharField(
        max_length=100,
        verbose_name='Stripe Charge Id'
    )
    amount = models.FloatField(default=0.0)
    object = models.CharField(max_length=100, blank=True, null=True)
    canceled_at = models.CharField(max_length=100, blank=True, null=True)
    cancellation_reason = models.TextField(blank=True, null=True)
    capture_method = models.CharField(max_length=100, blank=True, null=True)
    client_secret = models.CharField(max_length=255, blank=True, null=True)
    confirmation_method = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_payment_error = models.TextField(blank=True, null=True)
    livemode = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    payment_method_types = models.TextField(blank=True, null=True)
    receipt_email = models.CharField(max_length=100, blank=True, null=True)
    setup_future_usage = models.CharField(max_length=100, blank=True, null=True)
    shipping = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

