class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print('init methods executed...')
        self.get_response = get_response

    def __call__(self,request):
        print('pre processing of request')
        response = self.get_response(request)   # can you please forward the request to the next level
        print('post processing of request')
        return response
    # defined middleware and need to configure in settings.py
