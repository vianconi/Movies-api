from django.urls import path
from movie.views import get_movie, update_movie


app_name = 'movie'


urlpatterns = [
    path('', get_movie, name='movie'),
    path('<int:pk>', update_movie, name='movie'),
]

