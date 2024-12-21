from django.shortcuts import render

from library.models import Book

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, 'book_detail.html', context=context)