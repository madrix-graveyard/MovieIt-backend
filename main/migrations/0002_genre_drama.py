# Generated by Django 3.0.2 on 2020-01-18 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='drama',
            field=models.BooleanField(default=False),
        ),
    ]
