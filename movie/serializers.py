from rest_framework import serializers

from movie.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    release_date = serializers.DateField()
    duration = serializers.IntegerField()
    synopsis = serializers.CharField()

    def create(self, validated_date):
        validated_date.pop('id', None)
        movie = Movie.objects.create(**validated_date)
        return movie
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)

        instance.save()
        return instance
        