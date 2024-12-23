from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from cbv.models import User

from django.views.generic import ListView, DetailView

class MyView(View):
    def get(self, request):
        users = User.objects.all()
        users_list = [user.name for user in users] # add users objects to a list to show. if we had __str__ in model we could use users itself.
        show = ' '.join(users_list)
        return HttpResponse(show)

class UserListView(ListView):
    model = User # if we want to filter we can use this instead this line or use get_queryset function (commented in below): queryset = User.objects.filter(name='alireza')
    template_name = 'list.html' # send object to template with name: object_list. default template_name is 'cvb/User_list.html'
    paginate_by = 3 # shows every 3 object in a page. we will see every page with this query param (for example page 1): ?page=1

    # def get_queryset(self):
    #     return User.objects.filter(name='alireza')

class UserDetailView(DetailView):
    model = User # we can filter like ListView here too.
    template_name = 'detail.html' # send object to template with name: user. default template_name is 'cvb/User_detail.html'