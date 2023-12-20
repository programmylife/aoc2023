import urllib.request as request

url = 'https://pyrva.adamemery.dev/2016' # Set destination URL here

def get_request(url):
    return request.urlopen(url).read().decode()

def post_request(url, value):
    data = str.encode(str(value))
    req = request.Request(url, data)
    req.add_header('Content-Type', 'text/plain')
    return request.urlopen(req).read().decode()

directions = {
    'N': {
        'L': "W",
        'R': "E",
    },
    'E': {
        'L': "N",
        'R': "S",
    },
    'W': {
        'L': "S",
        'R': "N",
    },
    'S': {
        'L': "E",
        'R': "W",
    },
}

data = get_request(url)

def solution(data):
    current_direction = 'N'
    starting_point = [0,0]
    for val in data.split(','):
        direction, distance = val.strip()[0], int(val.strip()[1:])
        current_direction = directions[current_direction][direction]
        if current_direction == 'E':
            # positive x
            starting_point[0] += distance
        if current_direction == 'W':
            # negative x
            starting_point[0] -= distance
        if current_direction == 'S':
            # negative y
            starting_point[1] -= distance
        if current_direction == 'N':
            # positive y
            starting_point[1] += distance
        print(direction, distance, current_direction)
        print(starting_point)
        # breakpoint()
    return starting_point[0]+starting_point[1]


anwser = solution(data)
print(post_request(url, anwser))