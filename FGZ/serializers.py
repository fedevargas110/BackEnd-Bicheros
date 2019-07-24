from rest_framework import serializers
from FGZ.models import Animal, Ingreso

class AnimalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animal
    fields = '__all__'

  def to_representation(self, instance):
    ndeah = super().to_representation(instance)
    ndeah['gender'] = instance.get_gender_display()
    return ndeah

  def create(self, validated_data):
    return Animal.objects.create(**validated_data)
 
"""  def update(self, instance, validated_data):
    instance.id_animal = validated_data.get('ID', instance.id_animal)
    instance.save()
    return instance"""

class IngresoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingreso
    fields = '__all__'