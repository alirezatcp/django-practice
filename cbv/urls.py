from django.urls import path

from cbv.views import MyView, UserListView, UserDetailView

urlpatterns = [
    path('cbv/', MyView.as_view()),
    path('list_view/', UserListView.as_view()),
    path('detail_view/<int:pk>', UserDetailView.as_view())
]