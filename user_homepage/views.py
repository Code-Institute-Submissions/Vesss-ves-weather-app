import requests

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
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
    city = "London"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + settings.WEATHER_MAP_APP_ID

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city_name"]
        else:
            messages.error(request, "The city name is invalid!", extra_tags='danger')
    else:
        form = CityForm()
    r = requests.get(url.format(city)).json()

    if not r.get('main', None):
        city = "London"
        r = requests.get(url.format(city)).json()
        messages.warning(request, "The city has not been found! Please try again!")
    
    print(r)
    city_weather = {
        'city': city,
        'details': r['main'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'wind': r.get('wind',{}).get('speed'),
    }
    context = {'city_weather': city_weather, 'Form': form}

    return render(request, 'userhomepage.html', context, {'user': user})


def logout(request):
    """Log the user out"""
    auth.logout(request)
    return redirect(reverse('login'))
