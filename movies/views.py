from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieDataSerializer
from .models import MovieData
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type='action')
    serializer_class = MovieDataSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(type='comedy')
    serializer_class = MovieDataSerializer
