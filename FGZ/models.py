from django.db import models

# Create your models here.

GENDERS = (
  ('Masculino', 'Masculino'),
  ('Femenino', 'Femenino'),
)

class Animal(models.Model):
  id_animal = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  race = models.CharField(max_length=20)
  date_founded = models.DateField()
  place_founded = models.CharField(max_length=200)
  photo = models.ImageField(blank=True, upload_to='img/')
  species = models.CharField(max_length=120)
  gender = models.CharField(max_length=10, choices=GENDERS, default=0)
