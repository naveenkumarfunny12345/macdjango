from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_data_view(request):
    emp_data={
    'eno':100,
    'ename':'naveen',
    'esal':1000,
    'eaddr':'mumbai',
    }
    resp = '<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data={
    'eno':100,
    'ename':'naveen',
    'esal':1000,
    'eaddr':'mumbai',
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json') #Multipurpose Internet Mail Excemtion

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
    'eno':100,
    'ename':'naveen',
    'esal':1000,
    'eaddr':'mumbai',
    }
    #json_data=json.dumps(emp_data)
    return JsonResponse(emp_data) #Multipurpose Internet Mail Excemtion

#api develop needs class based method
# from django.views.generic import View
# class JsonCBV(View):
#     def get(self,request,*args,**kwargs):
#         emp_data={
#         'eno':100,
#         'ename':'naveen',
#         'esal':1000,
#         'eaddr':'mumbai',
#         }
#         #json_data=json.dumps(emp_data)
#         return JsonResponse(emp_data)


from django.views.generic import View
from testapp.mixins import HttpResponseMixin
class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from get method'})
        return self.render_to_http_response(json_data)
        # return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from post method'})
        return self.render_to_http_response(json_data)
        # call one instance method from another need self.method

    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from put method'})
        return self.render_to_http_response(json_data)

    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from delete method'})
        return self.render_to_http_response(json_data)
