from django.urls import path
from .views import StatisticsView, StatisticTitlesView

urlpatterns = [
    path('', StatisticsView.as_view(), name='statistics'),
    path('Titles/', StatisticTitlesView.as_view(), name='statisticTitles'),
]