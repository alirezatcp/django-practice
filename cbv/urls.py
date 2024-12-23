from django.urls import path

from cbv.views import MyView, UserListView

urlpatterns = [
    path('cbv/', MyView.as_view()),
    path('list_view/', UserListView.as_view())
]