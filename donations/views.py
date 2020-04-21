from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import redirect

# Create your views here.
    
class DonationPageView(TemplateView):
    template_name = 'donations.html'
    
    #def get(self, *args, **kwargs):
    #    return super().get(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        print(self.request.POST)
        return redirect("/")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_pub_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context