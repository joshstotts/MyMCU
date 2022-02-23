from django.db import models
from django.urls import reverse

# Create your models here.
class Favorite(models.Model):
    title = models.CharField(max_length=100)
    thoughts = models.CharField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'favorite_id': self.id})

class Watch(models.Model):
    date = models.DateField('Watch Date')
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)

    def __str__(self):
        return f'Watched on {self.date}'