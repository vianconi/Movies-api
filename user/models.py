from django.db import models
from django.contrib.auth.models import AbstractUser

from movie.models import Movie


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class RateMovie(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['user', 'movie']
        