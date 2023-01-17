from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
# import json   -- mixin will take care
from django.http import HttpResponse
# from django.core.serializers import serialize  --  mixins will take care
from testapp.mixins import SerializeMixin

# Create your views here.

#to get the records based on id:
class EmployeeDetailCBV(SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'The requested resource not available'})
        else:
            json_data=self.serialize([emp,])

        # emp_data = {
        # 'eno':emp.eno,
        # 'ename':emp.ename,
        # 'esal':emp.esal,
        # 'eaddr':emp.eaddr,
        # }
        # json_data=json.dumps(emp_data)    
        return HttpResponse(json_data,content_type='application/json')

# to get all the records
class EmployeeListCBV(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        # json_data=serialize('json',qs,fields=('eno','ename','eaddr'))
        # p_dict=json.loads(json_data)
        # final_list=[]
        # for obj in p_dict:
        #     emp_data=obj['fields']
        #     final_list.append(emp_data)
        # json_data=json.dumps(final_list)
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
