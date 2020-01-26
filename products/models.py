from django.db import models

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=130)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=4, null=39.99)
    