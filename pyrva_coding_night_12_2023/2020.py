import urllib.request as request
from math import floor

url = 'https://pyrva.adamemery.dev/2020' # Set destination URL here

def get_request(url):
    return request.urlopen(url).read().decode()

def post_request(url, value):
    data = str.encode(str(value))
    req = request.Request(url, data)
    req.add_header('Content-Type', 'text/plain')
    return request.urlopen(req).read().decode()



data = get_request(url)

def solution(data):    
    for value in data.split('\n'):
        if '\n'+str(2020 - int(value))+ '\n' in data:
            # breakpoint()
            print(int(value) * (2020-int(value)))
            return int(value) * (2020-int(value))

anwser = solution(data)
print(post_request(url, anwser))