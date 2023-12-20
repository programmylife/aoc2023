import urllib.request as request
from math import floor

url = 'https://pyrva.adamemery.dev/2019' # Set destination URL here

def get_request(url):
    return request.urlopen(url).read().decode()

def post_request(url, value):
    data = str.encode(str(value))
    req = request.Request(url, data)
    req.add_header('Content-Type', 'text/plain')
    return request.urlopen(req).read().decode()



data = get_request(url)

def solution(data):    
    result = 0
    for value in data.split('\n'):
        print(value)
        result += int(value) // 3 - 2
    # divide by 3, round down, subtract 2
    print(result)
    return result

anwser = solution(data)
print(post_request(url, anwser))