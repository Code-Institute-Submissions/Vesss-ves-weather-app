from django.shortcuts import render

from .models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    return render(request, "cart/cart.html", {})