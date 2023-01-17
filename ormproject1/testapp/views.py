from django.shortcuts import render,redirect
from testapp.models import Employee
# from testapp.forms import EmployeeForm
# Create your views here.
#CRUD ---> R - Retrive
def retrieve_view(request):
    emp_list = Employee.objects.()
    print(type(emp_list))
    return render(request,'testapp/index.html',{'emp_list':emp_list})

# return tyoe of all() method is : QuerySet
#<class 'django.db.models.query.QuerySet'>
# to get particlular record need get() method
# retur type(get method) is testapp.models.Employee
# python3 manage.py shell and practice
