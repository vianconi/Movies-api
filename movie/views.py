from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from movie.models import Movie
from movie.serializers import MovieSerializer

@swagger_auto_schema(method='POST', request_body=MovieSerializer)
@api_view(['GET', 'POST'])
def get_movie(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data, status=200)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    return Response({}, status=405)

@swagger_auto_schema(method='PUT', request_body=MovieSerializer)
@api_view(['PUT'])
def update_movie(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except:
        return Response('Not found', status=404)
 