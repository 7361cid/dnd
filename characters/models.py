from django.db import models
from django.urls import reverse


class Character(models.Model):
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    character_race = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('character', args=[str(self.id)])
