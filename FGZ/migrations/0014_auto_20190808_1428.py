# Generated by Django 2.2.3 on 2019-08-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0013_auto_20190806_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cap',
            name='age',
        ),
        migrations.AddField(
            model_name='cap',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
