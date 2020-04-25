from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Donation

import stripe
import json

    
class DonationPageView(TemplateView):
    template_name = 'donations.html'

    def get_context_data(self, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
          amount=1099,
          currency='usd',
          # Verify your integration in this guide by including this parameter
          #metadata={'integration_check': 'accept_a_payment'},
          setup_future_usage='off_session',
        )
        context = super().get_context_data(**kwargs)
        context['stripe_pub_key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['client_secret'] = intent.client_secret
        return context


class ThankYouPageView(TemplateView):
    template_name = 'thankyou.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, *args, **kwargs):
        post_data = json.loads(self.request.POST.get('data'))
        data = dict((key, post_data[key]) for key in post_data if key!='id')
        data["scid"] = post_data.get("id")
        print(data)
        don = Donation()
        
        for field, value in data.items():
            if hasattr(don, field):
                setattr(don, field, value)
        if self.request.user.is_authenticated:
            don.user = self.request.user
        don.save()
        return JsonResponse({"success": True})
        


class PaymentErrorPageView(TemplateView):
    template_name = 'payment_error.html'


