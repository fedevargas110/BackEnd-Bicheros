from rest_framework import serializers
from FGZ.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animal
    fields = '__all__'
