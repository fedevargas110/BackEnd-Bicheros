from django.db import models

# Create your models here.

GENDERS = (
  (0, 'Masculino'),
  (1, 'Femenino'),
)

class Animal(models.Model):
  id_animal = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  race = models.CharField(max_length=20)
  date_founded = models.DateField()
  place_founded = models.CharField(max_length=200)
  photo = models.ImageField(blank=True, upload_to='img/')
  species = models.CharField(max_length=120)
  gender = models.PositiveIntegerField(choices=GENDERS, default=0)

class CAP(models.Model):
  id_cap = models.AutoField(primary_key=True)
  nameC = models.CharField(max_length=20)
  last_nameC = models.CharField(max_length=20)
  age = models.CharField(max_length=20)
  address = models.CharField(max_length=120)