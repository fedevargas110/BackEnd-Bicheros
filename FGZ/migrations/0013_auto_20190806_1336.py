# Generated by Django 2.2.3 on 2019-08-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0012_auto_20190806_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='type_of_donation',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'comida de gato'), (1, 'comida de perro'), (2, 'ropa'), (3, 'otros')], default=0, null=True),
        ),
    ]
