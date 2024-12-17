from django.urls import path 

from app.views import welcome, index

urlpatterns = [
    path('say/welcome/', welcome),
    path('<str:first_name>/<str:last_name>/<int:age>/', index)
]