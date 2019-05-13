from rest_framework import serializers
from FGZ.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
  gender = serializers.SerializerMethodField()

  class Meta:
    model = Animal
    fields = '__all__'

  def get_gender(self, obj):
    return obj.get_gender_display()