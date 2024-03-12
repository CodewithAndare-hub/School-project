from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.home, name="home"),
        path('signup', views.signup, name="signup"),
        path('signin', views.signin, name="signin"),
        path('sign-out', views.sign_out, name="sign-out"),
        path('about', views.about, name="about"),
        path('services', views.services, name="services"),
        path('pin-generator', views.pin_generator, name="pin-generator"),
]
