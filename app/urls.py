from django.urls import path 

from app.views import welcome, index

urlpatterns = [
    path('say/welcome/', welcome),
    path('<str:name>/<int:age>/<slug:slug>/<uuid:uuid>/<path:path>/', index)
]