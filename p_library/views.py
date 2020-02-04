from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory  
from django.http.response import HttpResponseRedirect
from .models import Book, Author, Publisher, Friend
from .forms import AuthorForm, BookForm, FriendForm
import json
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView


def home(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))


class BookEdit(CreateView):  
    model = Book  
    form_class = BookForm  
    success_url = reverse_lazy('book_list') 
    template_name = 'book_add.html'

class BookList (ListView):  
    model = Book  
    template_name = 'book_list.html'
    context_object_name = 'book_list'


class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('author_list')
    template_name = 'authors_add.html'

class AuthorList (ListView):  
    model = Author  
    template_name = 'author_list.html'
    context_object_name = 'author_list'


class FriendEdit(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('friend_list')
    template_name = 'friend_add.html'

class FriendList (ListView):  
    model = Friend
    template_name = 'friend_list.html'
    context_object_name = 'friend_list'


class PublisherList (ListView):  
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'



def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            book.copy_count += 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/book/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/book/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/book/')
    else:
        return redirect('/book/')