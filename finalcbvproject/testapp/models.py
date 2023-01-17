from django.db import models
from django.urls import reverse

# Create your models here.
#1
class Beer(models.Model):
    name = models.CharField(max_length=128)
    taste = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    price = models.FloatField(max_length=128)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
