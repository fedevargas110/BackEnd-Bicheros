from rest_framework import serializers
from FGZ.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animal
    fields = '__all__'
  def to_representation(self, instance):
    ndeah = super().to_representation(instance)
    ndeah['gender'] = instance.get_gender_display()
    return ndeah