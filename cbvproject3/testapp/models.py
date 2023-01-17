from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    ceo = models.CharField(max_length=64)

# insert/delete button click seidhal , naan detail page poganum poi url paaru
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})  #current object poganum 'pk no hit aaganu'
