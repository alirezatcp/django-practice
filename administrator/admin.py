from django.contrib import admin

from administrator.models import Author, Book

# created a superuser with this command: python manage.py createsuperuser
# alireza, 123, a@gmail.com

admin.site.register(Book)
admin.site.register(Author)

