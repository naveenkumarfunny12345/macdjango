from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
    print(10/0)
    # if my db is  not running well
    # if any third party system is not working , you may get error
    return HttpResponse('<h1>Hello this is from view function</h1>')
