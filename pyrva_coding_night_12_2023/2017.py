import urllib.request as request

url = 'https://pyrva.adamemery.dev/2017' # Set destination URL here

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
    prev = None
    for value in data:
        if int(value) == prev:
            result += prev
        prev = int(value)
    print(result+2)
    return result+2


anwser = solution(data)
print(post_request(url, anwser))