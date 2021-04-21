# Generated by Django 3.1.7 on 2021-04-21 15:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 4, 21, 17, 48, 29, 424777))),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Statistics.statistictitle')),
            ],
        ),
    ]
