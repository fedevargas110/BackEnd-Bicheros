# Generated by Django 2.2.4 on 2019-08-22 13:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id_animal', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('race', models.CharField(blank=True, max_length=20, null=True)),
                ('date_founded', models.DateField(blank=True, null=True)),
                ('place_founded', models.CharField(blank=True, max_length=200, null=True)),
                ('species', models.CharField(blank=True, max_length=120, null=True)),
                ('gender', models.PositiveIntegerField(blank=True, choices=[(0, 'Masculino'), (1, 'Femenino')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CAP',
            fields=[
                ('id_cap', models.AutoField(primary_key=True, serialize=False)),
                ('nameC', models.CharField(blank=True, max_length=20, null=True, verbose_name='name')),
                ('last_nameC', models.CharField(blank=True, max_length=20, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id_donation', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=240, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('type_of_donation', models.PositiveIntegerField(blank=True, choices=[(0, 'comida de gato'), (1, 'comida de perro'), (2, 'remedios'), (3, 'cadenas'), (4, 'otros')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Monto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('tipo', models.PositiveIntegerField(blank=True, choices=[(0, 'Ingreso'), (1, 'Gasto')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinaria',
            fields=[
                ('id_veterinaria', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=270, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id_photo', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FGZ.Animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='cap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FGZ.CAP'),
        ),
        migrations.AddField(
            model_name='animal',
            name='veterinaria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FGZ.Veterinaria'),
        ),
    ]
