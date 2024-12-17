from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('Welcome.')

def index(requests, first_name, last_name, age):
    return HttpResponse(f'name: {first_name} {last_name}, age: {age}')