from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import User

# Create your views here.
def loginView(request):
    all_items=User.objects.all()
    return render(request, 'login.html', {'all_items': all_items})

def register(request):
    email = request.POST['email']
    password = request.POST['password']
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    dob = request.POST['dob']
    gender = False
    newUser = User(email=email, password=password, firstName=firstName, lastName=lastName, dob=dob, gender=gender)
    newUser.save()
    return HttpResponseRedirect('/login')

def auth(request):
    print(request.POST)
    email=request.POST['email']
    password=request.POST['password']
    user = User.objects.filter(email=email)
    
    if (len(user) == 0):
        return HttpResponse('invalid email')
    elif (user[0].password != password):
        return HttpResponse('wrong password')
    else:
        return HttpResponse('successful')