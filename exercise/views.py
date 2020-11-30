from django.shortcuts import render
from .models import Exercise, JoinExercise
import json
from django.core import serializers
from django.http import HttpRequest, HttpResponse

# Create your views here
def check_id(array_id, id):
    for i in array_id:
        if i == id:
            return True
    return False

def get_exercise(request, username):
    history = JoinExercise.objects.filter(completed=False)
    history_id = [i.exercise.id for i in history]
    new_exercises = Exercise.objects.exclude(check_id(history_id, id))

    data={'success':False}
    data['success']=True
    data['history'] = [i.toObject() for i in history]
    data['new_exercises'] = [i.toObject() for i in new_exercises]
    
    #data['all'] = [i.toObject() for i in all_exercise]
    #data['new_exercises'] = new_exercises
    return HttpResponse(json.dumps(data), content_type='application/json')