from django.http import Http404
from django.views.generic import ListView, DetailView

from cart.models import Cart
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = "products/products.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-details.html"

    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Error!")

        return instance
