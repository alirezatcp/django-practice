from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from cbv.models import User

class MyView(View):
    def get(self, request):
        users = User.objects.all()
        users_list = [user.name for user in users] # add users objects to a list to show. if we had __str__ in model we could use users itself.
        return HttpResponse(users_list)
