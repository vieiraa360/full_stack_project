"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from home import views
from home.views import index
from home.views import about
from blog import urls as urls_blog
from posts import urls as urls_posts
from posts.views import get_posts
from posts.views import post_detail
from testimonials import urls as urls_testimonials
from testimonials.views import get_testimonials
from testimonials.views import testimonial_detail
from testimonials.views import create_or_edit_testimonial
from posts.views import create_or_edit_post
from avatar import urls as avatar_urls
from accounts.views import editprofile
from checkout import urls as urls_checkout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faqs/', include(urls_posts)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^testimonials/', include(urls_testimonials)),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
