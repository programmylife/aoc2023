import urllib.request as request
from math import floor

url = 'https://pyrva.adamemery.dev/2023' # Set destination URL here

def get_request(url):
    return request.urlopen(url).read().decode()

def post_request(url, value):
    data = str.encode(str(value))
    req = request.Request(url, data)
    req.add_header('Content-Type', 'text/plain')
    return request.urlopen(req).read().decode()

data = get_request(url)
print(data)
print(post_request(url, "Yule,Gingerbread,Magi,Nutcracker,Tidings,Holly Jolly,Kris Kringle,Sleigh bells"))