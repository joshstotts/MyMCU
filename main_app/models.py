from django.db import models
from django.urls import reverse

# Create your models here.
class Favorite(models.Model):
    title = models.CharField(max_length=100)
    thoughts = models.CharField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'favorite_id': self.id})