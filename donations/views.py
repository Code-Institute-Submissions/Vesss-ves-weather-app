import stripe
import json

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Donation


class DonationPageView(TemplateView):
    # Donation page will be a public page
    template_name = 'donations.html'

    def get_context_data(self, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=1099,
            currency='usd',
            setup_future_usage='off_session',
        )
        context = super().get_context_data(**kwargs)

        # pass stripe credentials via context
        context['stripe_pub_key'] = settings.STRIPE_PUBLISHABLE_KEY
        context['client_secret'] = intent.client_secret
        return context


@method_decorator(decorator=[csrf_exempt, ], name='dispatch')
class ThankYouPageView(LoginRequiredMixin, TemplateView):
    template_name = 'thankyou.html'

    def post(self, *args, **kwargs):
        post_data = json.loads(self.request.POST.get('data'))
        data = dict((key, post_data[key]) for key in post_data if key != 'id')
        data["scid"] = post_data.get("id")
        # print(data)
        don = Donation()

        for field, value in data.items():
            # check the model attributes are matched and then save the values
            if hasattr(don, field):
                setattr(don, field, value)
        if self.request.user.is_authenticated:
            don.user = self.request.user
        don.save()
        return JsonResponse({"success": True})


class PaymentErrorPageView(LoginRequiredMixin, TemplateView):
    template_name = 'payment_error.html'
