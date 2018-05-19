from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from products.models import Product
# Create your tests here.


class CartViewsTests(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}
        self.request.anonymous_user = AnonymousUser()

    @classmethod
    def setUpTestData(cls):
        cls.test_product = Product(
            name='Testing Product',
            slug='testing-product',
            price=100,
            description='Lorem ipsum content',
        )

        cls.test_product.save()