from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ExampleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        content = {
            'message': 'request was permitted'
        }
        return Response(content)
    