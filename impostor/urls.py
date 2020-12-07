"""
Definition of urls for personalwebsite.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views
from . import views


urlpatterns = [
    #path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
]
