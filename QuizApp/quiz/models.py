from django.db import models

# Create your models here.
class Quiz(models.Model):
    qname=models.CharField(max_length=30)
    question1=models.CharField(max_length=5000)
    answer1=models.CharField(max_length=5000)
    question2=models.CharField(max_length=5000)
    answer2=models.CharField(max_length=5000)
    question3=models.CharField(max_length=5000)
    answer3=models.CharField(max_length=5000)
    question4=models.CharField(max_length=5000)
    answer4=models.CharField(max_length=5000)
    question5=models.CharField(max_length=5000)
    answer5=models.CharField(max_length=5000)