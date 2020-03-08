from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.utils.http import is_safe_url

# Create your views here.
def login(request):
    """Return a login page"""
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_po
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
                                    
            
            if user:
                auth.login(user=user, request=request)
                return redirect("user_homepage")
            
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "accounts/login.html", {"login_form": login_form})

def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {
        "registration_form": registration_form})
