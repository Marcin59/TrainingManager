from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Training
from django.core import serializers
import datetime
import re
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.
class AllTrainingsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AllTrainingsView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        trainings = Training.objects.all()
        response_data = serializers.serialize("json", trainings)
        return JsonResponse(response_data, safe=False)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        title = body['title']
        start = datetime.datetime.strptime(body['start'], "%Y-%m-%dT%H:%M:%S.%fZ")
        end = datetime.datetime.strptime(body['end'], "%Y-%m-%dT%H:%M:%S.%fZ")
        new_training = Training(title=title, start=start, end=end)
        new_training.save()

class TrainingsViewByDate(View):

    def get(self, request, *args, **kwargs):
        trainings = Training.objects.filter(date=datetime.datetime(year=self.kwargs['year'], month=self.kwargs['month'], day=self.kwargs['day']))
        response_data = serializers.serialize("json", trainings)
        return JsonResponse(response_data, safe=False)

class TrainingView(View):

    def get(self, request, *args, **kwargs):
        trainings = Training.objects.filter(pk=self.kwargs['pk'])
        response_data = serializers.serialize("json", trainings)
        return JsonResponse(response_data, safe=False)

class TrainingsViewByDateRange(View):

    def get(self, request, *args, **kwargs):
        #Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
        start_time = datetime.datetime.strptime(self.kwargs['start_date'], '%Y-%m-%d')
        end_time = datetime.datetime.strptime(self.kwargs['end_date'], '%Y-%m-%d')
        end_time += datetime.timedelta(days=1)
        trainings = Training.objects.filter(start__range=[start_time, end_time])
        response_data = serializers.serialize("json", trainings)
        return JsonResponse(response_data, safe=False)