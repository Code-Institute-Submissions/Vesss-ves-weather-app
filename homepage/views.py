from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
# from homepage.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')