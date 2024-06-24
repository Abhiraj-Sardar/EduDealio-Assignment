from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('login/signin/home/', views.home, name='home'),
]