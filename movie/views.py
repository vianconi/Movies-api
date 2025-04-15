from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from movie.models import Movie
from movie.serializers import MovieModelSerializer

class MoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieModelSerializer(movies, many=True)

        return Response(serializer.data, status=200)
    
    @swagger_auto_schema(request_body=MovieModelSerializer)
    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    @swagger_auto_schema(request_body=MovieModelSerializer)
    def put(self, request, pk=None):
        try:
            movie = Movie.objects.get(id=pk)
            serializer = MovieModelSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except:
            return Response('Not found', status=404)
 