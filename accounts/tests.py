from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from accounts.models import UserProfile
# Create your tests here.

class CartViewsTests(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.request.session = {}
        self.request.anonymous_user = AnonymousUser()

    @staticmethod
    def _create_testing_user():
        user = UserProfile(
            email='user@example.com',
            name='John',
            slug='John',
            is_active=True,
            is_admin=False,
            is_staff=False,
        )
        user.set_password(raw_password='@Pr0v1da')
        user.save()

        return user