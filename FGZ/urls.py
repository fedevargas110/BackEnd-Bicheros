from django.urls import path
from FGZ.views import *

urlpatterns = [
  path('Animal/', AnimalList.as_view(), name='animal')
  path('Monto/', MontoList.as_view(), name='monto')
  path('CAP/', CAPList.as_view(), name='cliente')
  path('Donacion/', DonacionlList.as_view(), name='donacion')
]