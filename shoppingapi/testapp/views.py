from django.shortcuts import render
from testapp.forms import AddItemForm
# Create your views here.

def add_item_view(request):
    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST['name']     # validation not done , so no used cleaned data
        quantity = request.POST['quantity']
        request.session[name]=quantity   # saved for future purpose
    return render(request,'testapp/additem.html',{'form':form})

def display_items_view(request):
    return render(request,'testapp/displayitems.html')
