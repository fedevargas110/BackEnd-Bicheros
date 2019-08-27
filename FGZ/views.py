from FGZ.models import Animal, Monto, CAP, Donacion, Veterinaria, Photo
from FGZ.serializers import AnimalSerializer, MontoSerializer, CAPSerializer, DonacionSerializer, VeterinariaSerializer, PhotoSerializer
from rest_framework import viewsets, permissions, status
from django.shortcuts import redirect
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class AnimalViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('name', 'gender')

class MontoViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = Monto.objects.all()
  serializer_class = MontoSerializer

class CAPViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = CAP.objects.all()
  serializer_class = CAPSerializer

  filter_backends = (filters.SearchFilter,)
  search_fields = ('nameC', 'last_nameC')

class DonacionViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = Donacion.objects.all()
  serializer_class = DonacionSerializer
  
  filter_backends = (filters.SearchFilter,)
  search_fields = ('type_of_donation',)

class VeterinariaViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = Veterinaria.objects.all()
  serializer_class = VeterinariaSerializer

  filter_backends = (filters.SearchFilter,)
  search_fields = ('name',)

class PhotoViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (TokenAuthentication, SessionAuthentication)
  queryset = Photo.objects.all()
  serializer_class = PhotoSerializer

  filter_backends = (filters.SearchFilter,)
  search_fields = ('animal__id_animal',)