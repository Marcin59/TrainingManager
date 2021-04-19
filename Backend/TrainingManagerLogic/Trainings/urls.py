from django.urls import path
from .views import TrainingsView, TrainingsViewByDateRange, ExerciseTitlesView, ExercisesViewByTrainingPk, SetsViewByExercisePk

urlpatterns = [
    path('', TrainingsView.as_view(), name='trainings'),
    path('ExerciseTitles/', ExerciseTitlesView.as_view(), name='exeriseTitles'),
    path('ExercisesByTrainingPk/<int:pk>/', ExercisesViewByTrainingPk.as_view()),
    path('SetsByExercisePk/<int:pk>/', SetsViewByExercisePk.as_view()),
    path('<str:start_date>/<str:end_date>/', TrainingsViewByDateRange.as_view(), name='trainingsbydate'),
]