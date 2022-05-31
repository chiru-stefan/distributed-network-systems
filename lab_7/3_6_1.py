import requests
import sys
from pprint import pprint


def get_api_key():
    with open(".env") as f:
        key = f.read()

    key = key.split('=')[1]
    return key.replace('\n', '')


def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(location[0], location[1],
                                                                                                       api_key)
    r = requests.get(url)
    return r.json()


def main():
    location = [44.2833, 28.5667]

    api_key = get_api_key()
    weather = get_weather(api_key, location)

    pprint(weather)


if __name__ == '__main__':
    main()
