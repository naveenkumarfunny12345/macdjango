from django.http import HttpResponse

class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response   # this line also not required , bcse to save the variable for future purpose
                # you can give pass also

    def __call__(self,request):  # just go to next  level is - view
        print('this line printed by first middleware-1 before processing the request')
        response =  self.get_response(request) # request comes to secongd middleware
        print('this line printed by first middleware-1 after processing the request')
        return response

class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response   # this line also not required , bcse to save the variable for future purpose
                # you can give pass also

    def __call__(self,request):  # just go to next  level is - view
        print('this line printed by first middleware-2 before processing the request')
        response =  self.get_response(request) # request comes to secongd middleware
        print('this line printed by first middleware-2 after processing the request')
        return response
