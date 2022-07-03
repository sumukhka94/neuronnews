from django.db import models

# Create your models here.

class Person(models.Model):
    Img = models.ImageField(upload_to='home/img/')