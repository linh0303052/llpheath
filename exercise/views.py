from django.shortcuts import render
from .models import Exercise, JoinExercise
import json
from django.core import serializers
from django.http import HttpRequest, HttpResponse

# Create your views here.

def get_exercise(request, username):
    history = JoinExercise.objects.filter(completed=False)
    new_exercises = Exercise.objects.all()

    data={'success':False}
    data['success']=True
    data['history'] = [i.toObject() for i in history]
    data['new_exercises'] = [i.toObject() for i in new_exercises]
    
    #data['all'] = [i.toObject() for i in all_exercise]
    #data['new_exercises'] = new_exercises
    return HttpResponse(json.dumps(data), content_type='application/json')