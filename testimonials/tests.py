from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Testimonial
from .models.Testimonial import Testimonial_text



class TestimonialsPageTests(SimpleTestCase):
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('get_testimonials'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials.html')
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse('testimonial_detail'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonialpost.html')



class TestimonialTests(TestCase):

    @classmethod
    def setUp(cls):
        Testimonial.objects.create(text='just a test')

    def test_content(self):
        Testimonial= Testimonial.text(id=1)
        expected_object_name = '{testimonial.text}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('testimonials'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'testimonials.html')