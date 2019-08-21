from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

GENDERS = (
  (0, 'Masculino'),
  (1, 'Femenino'),
)

TIPO = (
  (0, 'Ingreso'),
  (1, 'Gasto'),
)

DONATION = (
  (0, 'comida de gato'),
  (1, 'comida de perro'),
  (2, 'remedios'),
  (3, 'cadenas'),
  (4, 'otros'),
)

class Veterinaria(models.Model):
  id_veterinaria = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, blank=True, null=True)
  address = models.CharField(max_length=270, blank=True, null=True)
  phone = models.CharField(max_length=30, blank=True, null=True)
  email = models.EmailField(max_length=70, blank=True)

  def __str__(self):
    return '{}, {}'.format(self.name, self.address)

class CAP(models.Model):
  id_cap = models.AutoField(primary_key=True)
  nameC = models.CharField('name', max_length=20, blank=True, null=True)
  last_nameC = models.CharField('last name', max_length=20, blank=True, null=True)
  email = models.EmailField(max_length=70, blank=True)
  date_of_birth = models.DateField(blank=True, null=True)
  address = models.CharField(max_length=120, blank=True, null=True)
  telefono = models.CharField(max_length=30, blank=True, null=True)
  
class CAP(models.Model):
  id_cap = models.AutoField(primary_key=True)
  nameC = models.CharField(max_length=20)
  last_nameC = models.CharField(max_length=20)
  age = models.CharField(max_length=20)
  address = models.CharField(max_length=120)

  def __str__(self):
    return str(self.id_cap) + ' ' + str(self.nameC)


class Animal(models.Model):
  id_animal = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, blank=True, null=True)
  race = models.CharField(max_length=20, blank=True, null=True)
  date_founded = models.DateField(blank=True, null=True)
  place_founded = models.CharField(max_length=200, blank=True, null=True)
  photo = models.ImageField(blank=True, upload_to='img/', null=True)
  species = models.CharField(max_length=120, blank=True, null=True)
  gender = models.PositiveIntegerField(choices=GENDERS, default=0, blank=True, null=True)

  cap = models.ForeignKey(CAP, on_delete=models.CASCADE, null=True, blank=True)
  veterinaria = models.ForeignKey(Veterinaria, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):  
    return '{}, {}'.format(self.id_animal, self.name)

  cap = models.ForeignKey(CAP, on_delete=models.CASCADE, null=True, blank= True)

  def __str__(self):
    return str(self.id_animal) + ' ' + str(self.name)

class Monto(models.Model):
  date = models.DateField(blank=True, null=True)
  amount = models.FloatField(validators=[MaxValueValidator(9999999999)], blank=True, null=True)
  tipo = models.PositiveIntegerField(choices=TIPO, default=0, blank=True, null=True)
  
  def __str__(self):
    return '{}, {}, {}'.format(self.date, self.amount, self.tipo)

class Donacion(models.Model):
  id_donation = models.AutoField(primary_key=True)
  description = models.CharField(max_length=240, blank=True, null=True)
  date = models.DateField(blank=True, null=True)
  type_of_donation = models.PositiveIntegerField(choices=DONATION, default=0, blank=True, null=True)

  def __str__(self):  
    return '{}, {}'.format(self.description, self.date)