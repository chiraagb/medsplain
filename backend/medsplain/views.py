from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class DemoView(APIView):
    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content, status=status.HTTP_200_OK)
