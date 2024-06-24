from django.db import models

# Create your models here.
class Register(models.Model):
    uname=models.CharField(max_length=30)
    uemail=models.EmailField(max_length=35,unique=True)
    upass=models.CharField(max_length=20)
    udob=models.DateField()
    udesg = models.CharField(max_length=100)
    ucoins=models.IntegerField(default=10)
    uscore=models.IntegerField(default=0)
    urank=models.IntegerField(default=1000)