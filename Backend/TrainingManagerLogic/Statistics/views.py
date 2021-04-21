from django.shortcuts import render
from django.views import View
from .models import Statistic, StatisticTitle
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import datetime
import json

# Create your views here.
class StatisticsView(View):
    instance = Statistic

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(StatisticsView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        statistics = {}
        for title in StatisticTitle.objects.all():
            statistics[title.title] = []
            for data in title.statistic_set.all():
                new_data = {}
                new_data['weight'] = data.weight
                new_data['date'] = data.date
                statistics[title.title].append(new_data)
            statistics[title.title].sort(key=lambda x: x['date'])
        response_data = json.dumps(statistics, cls=DjangoJSONEncoder,)
        return JsonResponse(
            response_data,
            safe=False,
        )

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        print(body)
        weight = body["weight"]
        date = datetime.datetime.strptime(body['date'], "%Y-%m-%d")
        print(body["title"])
        title = StatisticTitle.objects.get(title=body["title"])
        newStatistic = self.instance(weight=weight, title=title, date=date)
        newStatistic.save()
        return HttpResponse('success')

class StatisticTitlesView(View):
    instance = StatisticTitle
    def get(self, request, *args, **kwargs):
        statisticTitles = self.instance.objects.all()
        response_data = serializers.serialize('json', statisticTitles)
        return JsonResponse(
            response_data,
            safe=False,
        )