from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/products.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()
        
class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-details.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product-details.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist.")
        return instance