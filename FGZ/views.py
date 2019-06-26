from FGZ.models import Animal
from FGZ.serializers import AnimalSerializer
from rest_framework import viewsets, permissions, status
from django.shortcuts import redirect
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import filters

class AnimalViewSet(viewsets.ModelViewSet):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer

  @action(methods=['GET', 'DELETE'], detail=True)
  def delete(self, request, pk, format=None):
      object = Animal.objects.get(pk=pk)
      object.delete()
      return redirect("../../")
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name',)
