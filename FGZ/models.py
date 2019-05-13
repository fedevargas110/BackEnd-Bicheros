from django.db import models

# Create your models here.

GENDERS = (
  (0, 'Male'),
  (1, 'Female'),
)

class Animal(models.Model):
  id_animal = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  race = models.CharField(max_length=20)
  date_founded = models.DateField()
  place_founded = models.CharField(max_length=200)
  photo = models.CharField(max_length=5)
  species = models.CharField(max_length=120)
  gender = models.PositiveIntegerField(choices=GENDERS, default=0)


