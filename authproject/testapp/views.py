from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')

def python_page_view(request):
    return render(request,'testapp/pythonexams.html')

def aptitude_page_view(request):
    return render(request,'testapp/aptitudeexams.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # form.save()  bcse of django security algorith.it cantWe  save plain password
        user = form.save()
        user.set_password(user.password) #now the user  object having encrypted password like pbkbs2,sha_256
        user.save() #now save this user object in the database
        return HttpResponseRedirect('/accounts/login')
    # for signup we dont have functionality like login
    return render(request,'testapp/signup.html',{'form':form})
