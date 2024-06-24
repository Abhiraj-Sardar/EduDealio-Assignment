from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('register/', views.register, name='register'),
     path('register/signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
     path('login/signin/', views.signin, name='signin'),
     
]