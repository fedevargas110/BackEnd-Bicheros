# Generated by Django 2.2.4 on 2019-10-24 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0010_animal_historia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='historia',
            new_name='history',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='temperamento',
            new_name='temperament',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='veterinaria',
            new_name='veterinary',
        ),
    ]