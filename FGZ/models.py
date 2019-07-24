from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

GENDERS = (
  (0, 'Masculino'),
  (1, 'Femenino'),
)

class Animal(models.Model):
  id_animal = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, blank=True, null=True)
  race = models.CharField(max_length=20, blank=True, null=True)
  date_founded = models.DateField(blank=True, null=True)
  place_founded = models.CharField(max_length=200, blank=True, null=True)
  photo = models.ImageField(blank=True, upload_to='img/', null=True)
  species = models.CharField(max_length=120, blank=True, null=True)
  gender = models.PositiveIntegerField(choices=GENDERS, default=0, blank=True, null=True)

  def __str__(self):
    return str(self.id_animal) + ' ' + str(self.name)


class CAP(models.Model):
  id_cap = models.AutoField(primary_key=True)
  nameC = models.CharField(max_length=20)
  last_nameC = models.CharField(max_length=20)
  age = models.CharField(max_length=20)
  address = models.CharField(max_length=120)

class Ingreso(models.Model):
  date = models.DateField(blank=True, null=True)
  amount_to_enter = models.IntegerField(validators=[MaxValueValidator(99999999999999999999)]) 