from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product-details.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
