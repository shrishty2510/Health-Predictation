from django.db import models

class Contactform(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=500)

# Create your models here.
