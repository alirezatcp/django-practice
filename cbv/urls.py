from django.urls import path

from cbv.views import MyView

urlpatterns = [
    path('cbv/', MyView.as_view())
]