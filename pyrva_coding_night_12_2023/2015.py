import urllib.request as request

url = 'https://pyrva.adamemery.dev/2015' # Set destination URL here

def get_request(url):
    return request.urlopen(url).read().decode()

def post_request(url, value):
    data = str.encode(str(value))
    req = request.Request(url, data)
    req.add_header('Content-Type', 'text/plain')
    return request.urlopen(req).read().decode()

data = get_request(url)

def get_floor(data):
    result = 0
    for char in data:
        if char == '(':
            result += 1
        elif char == ')':
            result -=1

    return result


anwser = get_floor(data)
print(post_request(url, anwser))