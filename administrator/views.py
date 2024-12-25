from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.forms.models import model_to_dict

from administrator.forms import SignUpForm, BookForm
from administrator.models import Book

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully.')

        return HttpResponse(f'{form.errors}')

    return HttpResponse('Only POST method allowed.')
    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwprd = request.POST['password']

        user = authenticate(request, username = username, password = passwprd)

        if user:
            dj_login(request, user)
            return HttpResponse('Login complete!')

        return HttpResponse('Wrong password or username!')

    return HttpResponse('Please login with post method.')

@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse('Please login first.')

        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if not request.user.check_password(old_password):
            return HttpResponse('Wrong old password.')
        
        if new_password1 != new_password2:
            return HttpResponse('Entered passwords are not identical.')

        request.user.set_password(new_password1)
        request.user.save()

        return HttpResponse('Password change successfully!')

    return HttpResponse('Only post method allowed.')


@csrf_exempt
@login_required(login_url='/login/') # check login and if user is not login go to /login/ page
def logout(request):
    if request.method == 'POST':

        # we used decorator instead this:
        # if not request.user.is_authenticated:
        #     return HttpResponse('Please login first.')

        dj_logout(request)

        return HttpResponse('Log out successfully!')

    return HttpResponse('Only post method allowed.')


# we should go to admin panel and select our user and go to User permissions and select "administrator | book | Can add book" to this user can add book.
@login_required(login_url='/login/')
@permission_required('administrator.add_book', raise_exception=True) # administrator: app name and add_book a code name.
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Book added successfully.')

        return HttpResponse(f'{form.errors}')

    return HttpResponse('Only post method allowed.')


# we should go to admin panel and select our user and go to User permissions and select "administrator | book | Can add book" to this user can change book.
@login_required(login_url='/login/')
@permission_required('administrator.change_book', raise_exception=True) 
@csrf_exempt
def change_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id = book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse('Book information updated.')

        return HttpResponse(f'{form.errors}')

    return HttpResponse('Only post method allowed.')


# we should go to admin panel and select our user and go to User permissions and select "administrator | book | Can add book" to this user can view book.
@login_required(login_url='/login/')
@permission_required('administrator.view_book', raise_exception=True) 
@csrf_exempt
def view_book(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, id=book_id)
        return HttpResponse(f'{model_to_dict(book)}') # shows models field in dict form
    return HttpResponse('Only get method allowed.')

