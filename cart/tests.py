from django.test import TestCase
from django.test import Client
from django.conf.urls import url
from .views import adjust_cart
# Create your tests here.


class Cart_Url_Test(TestCase):
    def test_details(self):
        response = self.client.get('/cart/')
        self.assertTrue(response.status_code, 200)
        
    def test_index(self):
            response = self.client.get('/')
            self.assertTrue(response.status_code, 200)