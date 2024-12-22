from django.shortcuts import render
from django.http import HttpResponse

from library.models import Book

from library.forms import BookForm

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'book_detail.html', context=context)

def books_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books_list.html', context=context)

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
        context = {'form' : form}
        return render(request, 'add_book.html', context)
        # books = Book.objects.all()
        # context = {'books': books}
        # return render(request, 'books_list.html', context=context)

    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book(author=data['author'], title=data['title'])
            book.save()
            return HttpResponse(book, status=201)

        return HttpResponse('Error', status=400)
