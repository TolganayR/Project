from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .models import *
from hotel import settings
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('offers', views.offers, name='offers'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('book', views.book, name='book')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)