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
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username