import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijsoncbv/'
resp = requests.post(BASE_URL+ENDPOINT)  # http request , returns in the form of json
data = resp.json()
print(data)  # json module gives in form of dictionary
