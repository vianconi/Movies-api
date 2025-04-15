from django.urls import path
from movie.views import MoviesView


app_name = 'movie'


urlpatterns = [
    path('', MoviesView.as_view(), name='movie')
]

