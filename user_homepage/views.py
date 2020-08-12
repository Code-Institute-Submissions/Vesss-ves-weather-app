import requests

from django.conf import settings
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CityForm


# Create your views here.
def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')


@login_required
def user_homepage(request):
    user = User.objects.get(email=request.user.email)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + settings.WEATHER_MAP_APP_ID

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city_name"]
            r = requests.get(url.format(city)).json()
            city_weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            context = {'city_weather': city_weather, 'Form': form}
    else:
        form = CityForm()
        city = "London"
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        context = {'city_weather': city_weather, 'Form': form}

    return render(request, 'userhomepage.html', context, {'user': user})


def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('login'))
