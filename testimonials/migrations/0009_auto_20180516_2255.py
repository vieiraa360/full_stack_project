# Generated by Django 2.0.4 on 2018-05-16 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0008_testimonial_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='user',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
