from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView

# Create your views here.
    
class DonationPageView(TemplateView):
    template_name = 'donations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = 'settings.STRIPE_PUBLISHABLE_KEY'
        return context