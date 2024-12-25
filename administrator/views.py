from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login

from administrator.forms import SignUpForm

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully.')

        return HttpResponse(f'{form.errors}')

    return HttpResponse('Only POST method allowed.')
    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwprd = request.POST['password']

        user = authenticate(request, username = username, password = passwprd)

        if user:
            dj_login(request, user)
            return HttpResponse('Login complete!')

        return HttpResponse('Wrong password or username!')

    return HttpResponse('Please login with post method.')