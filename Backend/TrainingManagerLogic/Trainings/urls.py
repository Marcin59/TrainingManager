from django.urls import path
from .views import AllTrainingsView, TrainingView, TrainingsViewByDate, TrainingsViewByDateRange

urlpatterns = [
    path('', AllTrainingsView.as_view(), name='trainings'),
    path('<int:pk>/', TrainingView.as_view(), name='training'),
    path('<int:year>/<int:month>/<int:day>/', TrainingsViewByDate.as_view(), name='trainingsbydate'),
    path('<str:start_date>/<str:end_date>/', TrainingsViewByDateRange.as_view(), name='trainingsbydate'),
]