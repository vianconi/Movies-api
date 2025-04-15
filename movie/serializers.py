from rest_framework import serializers

from movie.models import Movie
        

class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'duration', 'synopsis']
        