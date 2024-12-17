from django.urls import path 

from app.views import welcome

urlpatterns = [
    path('say/welcome/', welcome)
]