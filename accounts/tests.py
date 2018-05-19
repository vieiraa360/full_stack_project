from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from accounts.models import UserProfile
# Create your tests here.

class UserProfileTest(TestCase):
    def test_details(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        
    def test_index(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)