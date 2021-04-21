from django.shortcuts import render
from django.views import View
from .models import Statistic, StatisticTitle
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.
class StatisticsView(View):
    instance = Statistic
    def get(self, request, *args, **kwargs):
        statistics = {}
        for title in StatisticTitle.objects.all():
            statistics[title.name] = []
            for data in title.statistic_set.all():
                new_data = {}
                new_data['weight'] = data.weight
                new_data['date'] = data.start
                statistics[title.name].append(new_data)
            statistics[title.name].sort(key=lambda x: x['date'])
        response_data = json.dumps(statistics, cls=DjangoJSONEncoder,)
        return JsonResponse(
            response_data,
            safe=False,
        )