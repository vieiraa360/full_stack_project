from django.test import TestCase

# Create your tests here.

class Checkout_Url_Test(TestCase):
    def test_details(self):
        response = self.client.get('/checkout/')
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')