from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def display_view(request):
    # emp_list = Employee.objects.get_emp_sal_range(15000,20000)
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.get_emps_sorted_by('ename')
    emp_list = Employee.objects.get_emps_sorted_by('esal')
    return render(request,'testapp/index.html',{'emp_list':emp_list})

    # the person using my views becomes simple because of custom manager
