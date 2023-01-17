from django.http import HttpResponse
# class HttpResponseMixin(object): even we are not taking , its a child class of object only
class HttpResponseMixin:
    def render_to_http_response(self,json_data):
        #1000 lines of code 
        return HttpResponse(json_data,content_type='application/json')

# mixin is a class , this class contains several instance method , child classed can use this instanve method
