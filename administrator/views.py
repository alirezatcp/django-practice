from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout

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

@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first.')

        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if not request.user.check_password(old_password):
            return HttpResponse('Wrong old password.')
        
        if new_password1 != new_password2:
            return HttpResponse('Entered passwords are not identical.')

        request.user.set_password(new_password1)
        request.user.save()

        return HttpResponse('Password change successfully!')

    return HttpResponse('Only post method allowed.')

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first.')

        dj_logout(request)

        return HttpResponse('Log out successfully!')

    return HttpResponse('Only post method allowed.')