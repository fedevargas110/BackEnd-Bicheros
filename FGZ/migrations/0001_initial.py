# Generated by Django 2.2.1 on 2019-05-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id_animal', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('date_founded', models.DateField()),
                ('place_founded', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='img/')),
                ('species', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], default=0, max_length=10)),
            ],
        ),
    ]
