# Generated by Django 2.2.4 on 2019-08-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FGZ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='video',
            field=models.CharField(blank=True, max_length=270, null=True),
        ),
    ]
