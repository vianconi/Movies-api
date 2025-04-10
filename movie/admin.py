from django.contrib import admin
from movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration')
    search_fields = ['title']


admin.site.register(Movie, MovieAdmin)
