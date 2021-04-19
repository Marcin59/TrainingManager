from django.contrib import admin
from .models import Training, Exercise, ExerciseTitle, Set

# Register your models here.
admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(ExerciseTitle)
admin.site.register(Set)
