from django.http import HttpResponse

class AppMainenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response   # this line also not required , bcse to save the variable for future purpose
                # you can give pass also

    # no need to go to view function . its under maintenace
    def __call__(self,request):
        return HttpResponse('<h1>Currently application under maintenance..</h1>')
