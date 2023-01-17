from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
# Create your views here.
class CompanyListView(ListView):
    model = Company
    #default template file : company_list.html
    #default context object name: company_list


class CompanyDetailView(DetailView):
    model = Company
    #default template file : company_detail.html
    #default context object name: company or object

class CompanyCreateView(CreateView):
    model = Company
    #fields = ('name','location','ceo')  # which fields , we want the user to enter data
    fields = '__all__'
    #default template file: company_form.html

class CompanyUpdateView(UpdateView):
    model = Company
    #fields = ('name','location','ceo')  # which fields , we want the user to enter data
    fields = ('location','ceo')
    #default template file: company_form.html

from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = Company
    #after deleting the record , which url it should go
    success_url = reverse_lazy('list')  #this function will wait , untill deleting the record , poi urls paaru
    #default template file: company_form.html

    #i want to send a request to delete , go and declrae url for delete
