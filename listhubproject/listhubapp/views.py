# from django.shortcuts import render

# Create your views here.

# appname/views.py
from rest_framework import generics
from .models import ListHubProperty
from .serializers import ListHubPropertySerializer
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ListHubPropertyListView(generics.ListAPIView):
    serializer_class = ListHubPropertySerializer

    def get_queryset(self):
        two_days_ago = datetime.now() - timedelta(days=2)
        queryset = ListHubProperty.objects.filter(
            modified_date__gte=two_days_ago,
            # Add other criteria for residential properties
        )
        return queryset


class AddListHubPropertyView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ListHubPropertySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
