from django.urls import path
from FGZ.views import *

urlpatterns = [
  path('Animal/', AnimalList.as_view(), name='animal')
  path('Ingreso/', IngresoList.as_view(), name='ingreso')
]