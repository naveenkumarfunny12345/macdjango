from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Book
# # Create your views here.
# function based view
# def list_view(request):
#     books_list = Book.objects.all()
#     return render(request,'testapp/books.html',{'books_list':books_list})\

class BooklistView(ListView):
    model = Book
    #default template file : book_list.html
    #default context object name: book_list
    template_name = 'testapp/books.html'  # own template file
    context_object_name = 'books'     # own context_object_name
