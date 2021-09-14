from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication
# Create your views here.

class LibrosViewSet(ModelViewSet):
    permissions_classes = [AllowAny]
    serializer_class = serializers.LibrosSerializer

    def get_queryset(self):
        libros = models.Libros.objects.all()
        return libros