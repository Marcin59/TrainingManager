# Generated by Django 3.1.7 on 2021-04-06 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainings', '0005_auto_20210406_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 17, 40, 23, 606825)),
        ),
        migrations.AlterField(
            model_name='training',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 17, 40, 23, 606825)),
        ),
    ]
