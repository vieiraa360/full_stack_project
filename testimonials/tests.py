from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Testimonial
from .views import testimonial_detail, get_testimonials



class TestimonialsPageTests(TestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get('get_testimonials')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials.html')
        
    def test_view_url_by_name(self):
        response = self.client.get('testimonial_detail')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonialpost.html')
