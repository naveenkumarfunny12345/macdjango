from django.shortcuts import render
from firstApp.forms import StudentForm

def student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Record Inserted in to databases successfully')

    return render(request,'firstApp/studentform.html',{'form':form})



# Create your views here.
