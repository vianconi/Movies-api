from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    synopsis = models.TextField(default='No synopsis')

    def __str__(self):
        return f'{self.id} - {self.title}'
