import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id):
    resp=requests.get(BASE_URL+ENDPOINT+id+'/')
    print(resp.status_code)
    print(resp.json())
id=input('Enter some ID: ')
get_resource(id)

def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())
get_all()
