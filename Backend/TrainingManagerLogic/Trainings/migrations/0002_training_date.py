# Generated by Django 3.1.7 on 2021-03-31 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 31, 11, 14, 24, 310515)),
        ),
    ]