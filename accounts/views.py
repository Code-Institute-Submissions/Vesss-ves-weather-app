import stripe
from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.utils.http import is_safe_url

from .forms import UserLoginForm, UserRegistrationForm, AddressForm
from .models import BillingProfile

stripe.api_key = settings.STRIPE_SECRET_KEY


def login(request):
    """Return a login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user:
                # redirect logged in user to their homepage
                auth.login(user=user, request=request)
                return redirect("user_homepage")

            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        if request.user.is_authenticated:
            # if user is already logged in, then redirect to homepage
            return redirect('user_homepage')
        # send login form if it's get method and not logged in
        login_form = UserLoginForm()
    return render(request, "accounts/login.html", {"login_form": login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        # if user is already logged in, then redirect to homepage
        return redirect(reverse('user_homepage'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            # after a valid registration force user to login again
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password1']+'aslkdj;qwe'
            )
            if user:
                # auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!\nPlease login using the password you've just used")
                return redirect(reverse('login'))
            else:
                messages.error(request, "Unable to register your account at this time")
        else:
            messages.warning(request, registration_form.errors)
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {
        "registration_form": registration_form})


@login_required
def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, "billing/payment-method.html", {"publish_key": settings.STRIPE_SECRET_KEY, "next_url": next_url})


@login_required
def payment_method_create_view(request):
    if request.method == "POST" and request.is_ajax():
        # print(request.POST)
        return JsonResponse({"message": "Success! Your card was added!"})
    return HttpResponse("error", status_code=401)


@login_required
def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        instance = form.save(commit=False)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            address_type = request.POST.get('address_type', 'shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
            # print(address_type + "_address_id")
        else:
            messages.error(request, "Unexpected error!", 'danger')
            return redirect("cart:checkout")

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("cart:checkout")
    else:
        messages.error(request, form.errors, 'danger')
    return redirect("cart:checkout")
