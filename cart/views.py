import stripe
from urllib.parse import urljoin
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

from accounts.forms import UserLoginForm
from orders.models import Order
from products.models import Product
from addresses.models import Address
from addresses.forms import AddressForm
from .models import Cart
from billing.models import BillingProfile


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "cart/home.html", {"cart": cart_obj})


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home") #shortcurt for redirect
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
           cart_obj.products.remove(product_obj) 
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
        #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home") #shortcurt for redirect

def checkout_home(request):
    stripe_session_id = request.session.get('stripe_session_id')
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    login_form = UserLoginForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    
    billing_profile, billing_guest_profile_created = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        address_qs = Address.objects.filter(billing_profile=billing_profile)
        
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        request.session["order_obj_id"] = order_obj.id
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()
    
    # stripe integration
    if not stripe_session_id:
        try:
            order_obj_forStripe = Order.objects.get(cart=cart_obj)
            product_data_forStripe = []
            host_uri = "{}://{}".format(request.scheme, request.get_host())
            
            for item in order_obj_forStripe.cart.products.all():
                product_data_forStripe.append({
                    'name': item.title,
                    'description': item.description,
                    'images': [urljoin(host_uri, "media/"+str(item.image))],
                    'amount': int(item.price*100),
                    'currency': 'usd',
                    'quantity': 1,
                })
    
            # stripe checkout
            stripe.api_key = settings.STRIPE_SECRET_KEY
            
            stripeSession = stripe.checkout.Session.create(
              payment_method_types=['card'],
              line_items=product_data_forStripe,
              success_url=urljoin(host_uri, reverse("cart:success") + '?session_id={CHECKOUT_SESSION_ID}'),
              cancel_url=urljoin(host_uri, 'checkout/cancel'),
            )
            stripe_session_id = stripeSession.get('id')
            request.session['stripe_session_id'] = stripe_session_id
        except Order.DoesNotExist:
            # no need stripe if no order
            pass

    """
    # this section is now moved to checkout done or payment done view
    if request.method == "POST":
        "check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items']=0
            del request.session['cart_id']
            return redirect("cart:success")
    """
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "address_form": address_form,
        "address_qs": address_qs,
        "stripe_pub_key": settings.STRIPE_PUBLISHABLE_KEY,
        "stripe_session_id": stripe_session_id,
    }
    return render(request, "cart/checkout.html", context)
    

def checkout_done_view(request):
    order_obj_id = request.session.get("order_obj_id")
    if request.session.get('stripe_session_id') and request.session.get("order_obj_id") and request.session.get("cart_id"):
        try:
            order_obj = Order.objects.get(id=order_obj_id)
            
            "check that order is done"
            is_done = order_obj.check_done()
            if is_done:
                order_obj.mark_paid()
                request.session['cart_items']=0
                del request.session['cart_id']
                del request.session['stripe_session_id']
                return render(request, "cart/checkout-done.html", {})
        except Order.DoesNotExist:
            pass
    return redirect("cart:checkout")
    
    


