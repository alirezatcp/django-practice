from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse('Welcome.')

def index(requests, name, age, slug, uuid, path):
    return HttpResponse(f'str: {name}, int: {age}, slug: {slug}, uuid: {uuid}, path: {path}')
    # if this will be our url: http://127.0.0.1:8000/alireza/22/ascii_num/a07a1b13-c069-4eaf-836c-1f02be85bed8//path/to/a/file//
    # this will be result: str: alireza, int: 22, slug: ascii_num, uuid: a07a1b13-c069-4eaf-836c-1f02be85bed8, path: /path/to/a/file/