from django.shortcuts import render


def cart_home(request):
    # print(request.session)
    # print(dir(request.session))
    key = request.session.session_key
    print(key)
    return render(request, "cart/cart.html", {})