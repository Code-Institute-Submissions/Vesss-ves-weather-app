from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from accounts.forms import UserRegistrationForm


User = get_user_model()
client = Client()


class UserCreateTestCase(TestCase):
    """
    Checking user registration and login
    """
    def setUp(self):
        for i in range(0, 5):
            form_data = {
                'username': 'user_{}'.format(i),
                'email': 'user_{}@example.com'.format(i),
                'password1': 'AverySecretPa55',
                'password2': 'AverySecretPa55',
            }
            form = UserRegistrationForm(data=form_data)
            form.save()

    def test_forms(self):
        exist_user_form_data = {    # user data exists
            'username': 'user_0',
            'email': 'user_0@example.com',
            'password1': 'AverySecretPa55',
            'password2': 'AverySecretPa55',
        }
        exist_user_form = UserRegistrationForm(data=exist_user_form_data)

        non_exist_user_form_data = {    # new user data
            'username': 'user_5',
            'email': 'user_5@example.com',
            'password1': 'AverySecretPa55',
            'password2': 'AverySecretPa55',
        }
        non_exist_user_form = UserRegistrationForm(data=non_exist_user_form_data)

        self.assertFalse(exist_user_form.is_valid())
        self.assertTrue(non_exist_user_form.is_valid())

        # check login
        self.assertTrue(client.login(username=exist_user_form_data['username'], password=exist_user_form_data['password1']))
        self.assertFalse(client.login(username=exist_user_form_data['username'], password=exist_user_form_data['password1']+'not matched'))

