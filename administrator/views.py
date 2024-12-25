from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
        