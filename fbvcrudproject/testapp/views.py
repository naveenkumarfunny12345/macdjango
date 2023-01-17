from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.
#CRUD ---> R - Retrive
def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/index.html',{'emp_list':emp_list})


#CRUD ---> R - Insert

def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/insert.html',{'form':form})


# we have to get the record based on id , which django gives
#CRUD ---> R - Delete
def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance = employee)#i dont want empty form , i need data with the form to update
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee) # dont create new record,update in existing record
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'testapp/update.html',{'form':form})
