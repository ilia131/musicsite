from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadmusicSerializer
from .models import Uploadmusic


class UploadmusicView(APIView):
    def get(self, request):
        queryset = Uploadmusic.objects.all()
        serializer = UploadmusicSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UploadmusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)