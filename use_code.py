import requests


def get_points_from_server(endpoint):
    result = requests.request('get', f'{endpoint}/load')
    if result.status_code != 200:
        raise Exception()
    result = requests.request('get', f'{endpoint}/points')
    if result.status_code != 200:
        raise Exception()
    pass


get_points_from_server('http://127.0.0.1:5000/')
