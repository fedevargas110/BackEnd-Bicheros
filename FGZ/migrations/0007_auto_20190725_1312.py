# Generated by Django 2.2.3 on 2019-07-25 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0006_auto_20190724_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount_to_enter', models.IntegerField(null=True, validators=[django.core.validators.MaxLengthValidator(20)])),
                ('tipo', models.PositiveIntegerField(blank=True, choices=[(0, 'Ingreso'), (1, 'Gasto')], default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Ingreso',
        ),
    ]