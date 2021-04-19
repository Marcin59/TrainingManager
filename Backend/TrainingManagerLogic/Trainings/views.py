from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Training, ExerciseTitle, Exercise, Set
from django.core import serializers
import datetime
import re
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.
class TrainingsView(View):
    instance = Training

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TrainingsView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        trainings = self.instance.objects.all()
        response_data = serializers.serialize("json", trainings)
        return JsonResponse(response_data, safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        start = datetime.datetime.strptime(body['start'], "%Y-%m-%d %H:%M")
        newTraining = self.instance(title=body['title'], start=start, end=start)
        newTraining.save()
        for exercise in body['exercises']:
            newExercise = newTraining.exercise_set.create(title=ExerciseTitle.objects.get(title=exercise['title']))
            for set in exercise['sets']:
                newExercise.set_set.create(reps=set['reps'],
                                            weight=set['weight'])

    def delete(self, request, *args, **kwargs):
        body = json.loads(request.body)
        training = self.instance.objects.get(pk=body['pk'])
        training.delete()


class TrainingsViewByDateRange(View):

    def get(self, request, *args, **kwargs):
        start_time = datetime.datetime.strptime(self.kwargs['start_date'], '%Y-%m-%d')
        end_time = datetime.datetime.strptime(self.kwargs['end_date'], '%Y-%m-%d')
        end_time += datetime.timedelta(days=1)
        trainings = Training.objects.filter(start__range=[start_time, end_time])
        response_data = serializers.serialize("json", trainings)
        return JsonResponse(response_data, safe=False)

class ExerciseTitlesView(View):
    instance = ExerciseTitle

    def get(self, request, *args, **kwargs):
        exercise_titles = self.instance.objects.all()
        response_data = serializers.serialize("json", exercise_titles)
        return JsonResponse(response_data, safe=False)

class ExercisesViewByTrainingPk(View):
    instance = Exercise

    def get(self, request, *args, **kwargs):
        training = Training.objects.get(pk=self.kwargs['pk'])
        exercises = self.instance.objects.filter(training=training)
        response_data = serializers.serialize("json", exercises)
        return JsonResponse(response_data, safe=False)

class SetsViewByExercisePk(View):
    instance = Set

    def get(self, request, *args, **kwargs):
        exercise = Exercise.objects.get(pk=self.kwargs['pk'])
        sets = self.instance.objects.filter(exercise=exercise)
        response_data = serializers.serialize("json", sets)
        return JsonResponse(response_data, safe=False)