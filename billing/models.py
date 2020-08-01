from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
import stripe

User = settings.AUTH_USER_MODEL


class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        created = False
        obj = None
        if user.is_authenticated():
            'logged in user checkout; remember payment stuff'
            obj, created = BillingProfile.objects.get_or_create(
                                    user=user, email=user.email)
        else:
            pass
        return obj, created

# Create your models here.
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)
    
    objects = BillingProfileManager()
    
    def __str__(self):
        return self.email
        
def billing_profile_created_receiver(sender, instance, *args, **kwargs):
        if not instance.customer_id and instance.email:
            print("ACTUAL API REQUEST Send to Stripe")
            customer = stripe.Customer.create(
            email = instance.email
                )
            print(customer)
            instance.customer_id = customer.id

pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)
        
post_save.connect(user_created_receiver, sender=User)
    
    
    
