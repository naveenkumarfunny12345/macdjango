from django.http import HttpResponse

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response   # this line also not required , bcse to save the variable for future purpose
                # you can give pass also


    def __call__(self,request):  # just go to next  level is - view
        response =  self.get_response(request)
        return response

# if any business logic error(view) - use this
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>Currentlytechnical problem..<br>The Raised Exceptions:{exception.__class__.__name__} <br>The exception message:{exception} try afte</h1>')
        
