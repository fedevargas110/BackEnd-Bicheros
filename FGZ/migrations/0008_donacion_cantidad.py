# Generated by Django 2.2.4 on 2019-08-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0007_historialm_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='donacion',
            name='cantidad',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]