from rest_framework import serializers
from FGZ.models import Animal, Monto, CAP, Donacion, Veterinaria, Photo

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

class MontoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Monto
    fields = '__all__'

  def to_representation(self, instance):
    troll = super().to_representation(instance)
    troll['tipo'] = instance.get_tipo_display()
    return troll

class CAPSerializer(serializers.ModelSerializer):
  class Meta:
    model = CAP
    fields = '__all__'

class DonacionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Donacion
    fields = '__all__'

  def to_representation(self, instance):
    epico = super().to_representation(instance)
    epico['type_of_donation'] = instance.get_type_of_donation_display()
    return epico  

class VeterinariaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Veterinaria
    fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Photo
    fields = '__all__'