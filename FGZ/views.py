from FGZ.models import Animal, Ingreso
from FGZ.serializers import AnimalSerializer, IngresoSerializer
from rest_framework import viewsets, permissions, status
from django.shortcuts import redirect
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import filters

class AnimalViewSet(viewsets.ModelViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name',)

class IngresoViewSet(viewsets.ModelViewSet):
  queryset = Ingreso.objects.all()
  serializer_class = IngresoSerializer
