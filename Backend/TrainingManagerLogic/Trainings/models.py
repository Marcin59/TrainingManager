from django.db import models
import datetime

# Create your models here.
class Training(models.Model):
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

class ExerciseTitle(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

class Exercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    title = models.ForeignKey(
        ExerciseTitle,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.pk}'

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.pk}'