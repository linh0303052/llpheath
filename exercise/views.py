from django.shortcuts import render
from .models import Exercise, JoinExercise
import json
# Create your views here.

def get_exercise(request, username):
    #history = Exercise.objects.filter(joinexercise__completed=False, joinexercise__user__username = username)
    all_exercise = Exercise.objects.all()
    # new_exercises = Exercise.objects.filter(self not in history)
    data['success']=True
    # data['history'] = history
    data['all'] = all_exercise
    #data['new_exercises'] = new_exercises
    return HttpResponse(json.dumps(data), content_type='application/json')