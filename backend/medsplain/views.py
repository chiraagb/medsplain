from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from medsplain.models import Medication

# Create your views here.


# write a simple view that returns a string
# def home(request):
#     return JsonResponse({"message": "Hello, world!"})


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"


class HomeView(APIView):
    # class SampleSerializer(serializers.Serializer):
    #     name = serializers.CharField()
    #     id = serializers.IntegerField()

    class SampleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Medication
            fields = "__all__"

    def get(self, request):
        one = Medication.objects.first()
        serializer = self.SampleSerializer(one)
        # return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.SampleSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = SampleSerializer
    queryset = Medication.objects.all()
