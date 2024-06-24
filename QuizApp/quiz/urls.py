from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('login/signin/quiz/', views.quiz, name='quiz'),
     path('quiz/', views.quizHome, name='quizhome'),
     path('quiz/<str:qname>/<str:qno>/', views.quizpage, name='quizpage'),

]