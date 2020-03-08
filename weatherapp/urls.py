"""weatherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf 
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from user_homepage.views import user_homepage, logout
from homepage.views import index
from accounts.views import login, registration
from donations import views as donation_views
from products.views import ProductListView, ProductDetailView, ProductFeaturedDetailView, ProductFeaturedListView, ProductDetailSlugView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^userhomepage/$', user_homepage, name="user_homepage"),
    url(r'^$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^cart/', include("cart.urls", namespace="cart")),
    url(r'^products/$', ProductListView.as_view(), name="products"),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^registration/$', registration, name="registration"),
    url(r'^donate/$', donation_views.DonationPageView.as_view(), name="donations")
]
