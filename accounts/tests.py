from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from .models import UserProfile
from .forms import UserLoginForm
from django.test import Client
from .forms import *
# Create your tests here.

class UserProfile_Test(TestCase):
    def test_details(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        
    def test_index(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)




class LogIn_Test(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response['user'].is_authenticated)
        


class Setup_Class(TestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@mp.com", password="user", first_name="user", lastname="user")

class UserForm_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': "user", 'first_name': "user", 'last_name': "user"})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
        self.assertFalse(form.is_valid())