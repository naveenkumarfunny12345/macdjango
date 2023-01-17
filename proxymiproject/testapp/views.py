from django.shortcuts import render
from testapp.models import *

# Create your views here.

def display_view(request):
    # emp_list= Employee.objects.all()
    emp_list= ProxyEmployee1.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})

# if you want different views for the same table go for proxy model inheritance
