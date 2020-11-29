from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Account
from django.contrib.auth import authenticate, login
import random
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.dateparse import parse_date

import json

# Create your views here.
@csrf_exempt
def loginView(request):
    all_items = Account.objects.all()
    return render(request, 'login.html', {'all_items': all_items})


@csrf_exempt
def register(request):
    username = request.POST['username']
    email = request.POST['email']
    user = Account.objects.filter(username=username)
    if (len(user) > 0):
        data = {'success': False,
                'message': 'Username existed!'}
        return HttpResponse(data)

    user = Account.objects.filter(email=email)
    if (len(user) > 0):
        data = {'success': False,
                'message': 'Username existed!'}
        return HttpResponse(data)

    password = request.POST['password']
    if (hasattr(request.POST,'first_name')):
        firstName = request.POST['first_name']
    else:
        firstName = 'No'
    if (hasattr(request.POST,'last_name')):
        lastName = request.POST['last_name']
    else:
        lastName = 'Name'
    dob = parse_date(request.POST['dob'])
    print(dob.)
    if (hasattr(request.POST,'weight')):
        weight = request.POST['weight']
    else:
        weight = 0
    if (hasattr(request.POST,'height')):
        height = request.POST['height']
    else:
        height = 0
    if (hasattr(request.POST,'male')):
        gender = True
    else:
        gender = False
    newAccount = Account.objects.create_user(username=username, email=email, password=password,
                                             first_name=firstName, last_name=lastName, dob=dob, gender=gender,
                                             weight=weight, height=height)
    if (newAccount is not None):
        data = {'success': True}
    else:
        data = {'success': False}
    return HttpResponse(data)

@csrf_exempt
def auth(request):
    print(request.content_type)
    data = {'success': False}
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_login(request, login_form.get_user())
            data['success'] = True
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def forgot_password(request):
    data = {'success': False}
    chars = 'abcdefghiklmnopqrstuvwxyz1234567890ABCDEFGHIKLMNOPQRSTUVWXYZ'
    password = ''
    for i in range(0, 8):
        password += random.choice(chars)
    username = request.POST['username']

    user = Account.objects.filter(username=username)
    if (len(user) == 0):
        data.message = 'username does not exist'
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    last_name = user.last_name
    email = user.email
    user.set_password(password)
    send_mail(
        subject='[LLP Health] Reset password',
        message='''Dear {},
                    Your password has been changed to:{}
                    Log in with this new password and then change to another.
                    Best regards.'''.format(last_name, password)
        recipient_list=[email],
        from_email='ltt.lop9a1.lhlinh@gmail.com'
    )
    data.success = True
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def change_password(request):
    data = {'success': False}
    username = request.POST['username']
    old_password = request.POST['old_pasword']
    new_password = request.POST['new_password']
    user = Account.objects.get(username=username)
    if (user.check_password(old_password)):
        user.set_password(new_password)
        data.success = True
    else:
        data.message = 'wrong password'
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def getUser(request):
    data = {'success': False}
    username = request.POST['username']
    user = Account.objects.get(username=username)
    data.dob = user.dob
    data.first_name = user.first_name
    data.last_name = user.last_name
    data.email = user.email
    data.success = True
    return HttpResponse(json.dumps(data), content_type='application/json')