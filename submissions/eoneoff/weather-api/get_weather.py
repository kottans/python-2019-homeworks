import requests
from datetime import datetime

_baseUrl = 'http://api.openweathermap.org/data/2.5/'

_params = {'APPID': 'c4ad7974f3977f8f388a60b5c0267caa'}

def get_weather(mode, location, units):
    _params['q'] = location
    _params['units'] = units
    data = requests.get(url=f'{_baseUrl}{mode}', params=_params).json()
    return [_make_weather_data(data, data['name'])] if mode=='weather' \
        else [_make_weather_data(day, data['city']['name']) for day in data['list']]



def _make_weather_data(data, name):
    return {
        'icon': data['weather'][0]['icon'],
        'city': name,
        'date': datetime.fromtimestamp(data['dt']),
        'description': data['weather'][0]['description'],
        'temp': data['main']['temp'],
        'maxTemp': data['main']['temp_max'],
        'minTemp': data['main']['temp_min'],
        'wind': {
            'deg': data['wind']['deg'],
            'speed': data['wind']['speed']
        }
    }