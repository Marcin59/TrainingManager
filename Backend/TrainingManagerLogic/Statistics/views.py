from django.shortcuts import render
from django.views import View
from .models import Statistic
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
class StatisticsView(View):
    instance = Statistic
    def get(self, request, *args, **kwargs):
        statistics = self.instance.objects.all()
        response_data = serializers.serialize("json", statistics)
        return JsonResponse(response_data, safe=False)