# Generated by Django 2.2.3 on 2019-07-24 14:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0005_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso',
            name='amount_to_enter',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999999999999)]),
        ),
    ]
