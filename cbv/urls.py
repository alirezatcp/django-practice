from django.urls import path

from cbv.views import MyView, UserListView, UserDetailView, UserCreateView, UserCreateFormView, UserDeleteView

urlpatterns = [
    path('cbv/', MyView.as_view(), name='cbv'),
    path('list_view/', UserListView.as_view()),
    path('detail_view/<int:pk>', UserDetailView.as_view()),
    path('create_view/', UserCreateView.as_view()),
    path('form_view/', UserCreateFormView.as_view()),
    path('delete_view/<int:pk>', UserDeleteView.as_view()),
]