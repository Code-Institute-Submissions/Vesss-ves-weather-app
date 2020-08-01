from django.contrib import admin

from .models import Address, BillingProfile


admin.site.register(Address)
admin.site.register(BillingProfile)
