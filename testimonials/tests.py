from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse



class TestimonialsPageTests(SimpleTestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('get_testimonials'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials.html')
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse('testimonial_detail'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonialpost.html')


