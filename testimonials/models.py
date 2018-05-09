from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

class Testimonial(models.Model):

    title = models.CharField(max_length=50, null=True)
    text = models.TextField()
    author = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100, blank=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    active = models.BooleanField(default=False)
