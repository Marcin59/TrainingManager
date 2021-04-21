from django.db import models
import datetime

# Create your models here.
class StatisticTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

class Statistic(models.Model):
    title = models.ForeignKey(StatisticTitle, on_delete=models.CASCADE)
    weight = models.FloatField()
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.title} {self.weight}kg'