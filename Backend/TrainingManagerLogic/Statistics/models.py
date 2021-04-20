from django.db import models
import datetime

# Create your models here.
class StatisticTitle(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Statistic(models.Model):
    name = models.ForeignKey(StatisticTitle, on_delete=models.CASCADE)
    weight = models.FloatField()
    start = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.name} {self.weight}kg'