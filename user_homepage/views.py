import requests
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Form
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')


def user_homepage(request, name="userhomepage"):
    user = User.objects.get(email=request.user.email)
    profile = {'user': user}
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=38e4fec38e509c018629074ac1754906'

    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city_name"]
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            result = {'city_weather': city_weather, 'Form': form}

    else:
        form = Form()
        city = "London"
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        result = {'city_weather': city_weather, 'Form': form}

    return render(request, 'userhomepage.html', result, profile)


def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('index'))
