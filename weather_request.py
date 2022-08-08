from tkinter import *
from tkinter import messagebox
import requests

def get_weather(city):
    key = '0925f2864ae4e93b78b07bbb7f5c6052'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather_json = result.json()
    if weather_json["cod"]!='404':
        str1 = f'температура {weather_json["main"]["temp"]} С\n \
            чувствуется {weather_json["main"]["feels_like"]} С\n \
            ветер {weather_json["wind"]["speed"]} м/с \n \
            давление {weather_json["main"]["pressure"]} рт.ст.\n \
            влажность {weather_json["main"]["humidity"]} %\n \
                '
    else:
        str1='нет такого города'                
    return str1

#get_weather('Moscow')