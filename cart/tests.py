from django.test import TestCase

from accounts.forms import UserRegistrationForm
from .models import Cart, Product


class CartUpdateTestCase(TestCase):
    """
    Check if cart updating the products price correctly
    """
    user = None
    products = []

    def setUp(self):
        form_data = {
            'username': 'user_A',
            'email': 'user_A@example.com',
            'password1': 'AverySecretPa55',
            'password2': 'AverySecretPa55',
        }

        form = UserRegistrationForm(data=form_data)
        self.user = form.save()

        self.products.append(Product.objects.create(title='sample prod 1', slug='abc', description='dummy description', price=50))
        self.products.append(Product.objects.create(title='sample prod 2', slug='abcde', description='dummy description', price=100))

    def test_cart_update(self):
        cart = Cart.objects.create(
            user=self.user,
        )
        cart.products.add(self.products[0])
        cart.products.add(self.products[1])
        cart.save()
        self.assertEqual(cart.subtotal, self.products[0].price + self.products[1].price)
