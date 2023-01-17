from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request, 'testapp/home.html')


def age_view(request):
    print(request.COOKIES)
    username = request.GET['name']
    response = render(request, 'testapp/age.html', {'name':username})
    response.set_cookie('name',username)     #name of the cookie ,value of the cookie
    return response

def gf_view(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.GET['age']
    response = render(request, 'testapp/gf.html', {'name':username})
    response.set_cookie('age',age) # age is needed fr future purpose
    return response

def results_view(request):
    print(request.COOKIES)
    username = request.COOKIES['name']
    age = request.COOKIES['age']
    gfname = request.GET['gf']
    response = render(request, 'testapp/results.html', {'name':username,'age':age,'gf':gfname})
    response.set_cookie('gf',gfname) # age is needed fr future purpose
    return response
