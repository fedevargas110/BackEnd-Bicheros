# Generated by Django 2.2.3 on 2019-07-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0004_auto_20190618_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('amount_to_enter', models.IntegerField()),
            ],
        ),
    ]
