from django.db import models
import datetime

# Create your models here.
class Training(models.Model):
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'