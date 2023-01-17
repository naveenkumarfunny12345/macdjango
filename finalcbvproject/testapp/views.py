from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Beer

# Create your views here.
class BeerListView(ListView):
    model = Beer
    #default template file +beer_list.html
    #c_o_n = beer_list


class BeerDetailView(DetailView):#1
    model = Beer
    #default template file beer_detail.html  #2
    #c_o_n = beer or object

class BeerCreateView(CreateView):#1
    model = Beer
    fields = '__all__'
    #default template file beer_form.html  #2
    #c_o_n = beer or object

class BeerUpdateView(UpdateView):#1
    model = Beer
    fields = '__all__'
    #default template file beer_form.html  #2
    #c_o_n = beer or object

from django.urls import reverse_lazy
class BeerDeleteView(DeleteView):#1
    model = Beer
    success_url = reverse_lazy('list')
    #default template file beer_form.html  #2
    #c_o_n = beer or object
