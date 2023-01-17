from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    pages = models.IntegerField(max_length=300)
    price = models.FloatField(max_length=300)
