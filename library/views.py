from django.shortcuts import render

from library.models import Book

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'book_detail.html', context=context)

def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books_list.html', context=context)