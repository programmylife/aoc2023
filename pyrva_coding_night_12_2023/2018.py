import urllib.request as request

url = 'https://pyrva.adamemery.dev/2018' # Set destination URL here

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
        if value[0] == '+':
            result += int(value[1:])
        elif value[0] == '-':
            result -= int(value[1:])
        print(result)
    return result

anwser = solution(data)
print(post_request(url, anwser))