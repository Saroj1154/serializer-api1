import requests

#use the endpoint that you need : See endpoints from urls.py file
URL_endpoint = "http://127.0.0.1:8000/stuinfo"

r = requests.get(url=URL_endpoint)
data = r.json()
print(data)

