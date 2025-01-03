from administrator.views import signup, login, change_password, logout, add_book, change_book, view_book, delete_book, hide_book
# from app.views import welcome

from django.urls import path

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('passwd/', change_password),
    path('logout/', logout),
    
    path('add_book/', add_book),
    path('change_book/<int:book_id>/', change_book),
    path('view_book/<int:book_id>/', view_book),
    path('delete_book/<int:book_id>/', delete_book),
    path('hide_book/<int:book_id>/', hide_book),
]
