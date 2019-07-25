from FGZ.models import Animal, Monto
from FGZ.serializers import AnimalSerializer, MontoSerializer
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

class MontoViewSet(viewsets.ModelViewSet):
  queryset = Monto.objects.all()
  serializer_class = MontoSerializer
