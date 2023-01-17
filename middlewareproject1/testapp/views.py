from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome_view(request):
    print('this line added by view function')
    return HttpResponse('<h1>custom middleware Demo </h1>')
