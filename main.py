import requests


def get_request():
    response = requests.get('URL')
    json_response = response.json()
    print(json_response)
    return json_response


if __name__ == '__main__':
    get_request()
