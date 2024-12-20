from django.shortcuts import render
from django.http import HttpResponse

def welcome(request): 
    fname = request.GET.get('firstname') or '' # we will get this in request with query params. if we send nothing in query params as fname it sets ''
    lname = request.GET.get('lastname') # we will get this in request with query params. if we send nothing in query params as lname it sets None
    # something = request.GET['thing'] #  we will get this in request with query params. if we send nothing in query params as thing, we will get error.
    return HttpResponse(f'Welcome, {fname} {lname}') # now i should use a url like this: http://127.0.0.1:8000/say/welcome/?firstname=alireza&lastname=taaty

def index(requests, name, age, slug, uuid, path):
    return HttpResponse(f'str: {name}, int: {age}, slug: {slug}, uuid: {uuid}, path: {path}')
    # if this will be our url: http://127.0.0.1:8000/alireza/22/ascii_num/a07a1b13-c069-4eaf-836c-1f02be85bed8//path/to/a/file//
    # this will be result: str: alireza, int: 22, slug: ascii_num, uuid: a07a1b13-c069-4eaf-836c-1f02be85bed8, path: /path/to/a/file/