from get_weather import get_weather
from icons import icons
from terminaltables import SingleTable
from color import c
from manage_cities import save_city
from wrong_city import wrong_city

def show_weather(mode, location, units):
    weather = {}
    while not weather:
        try:
            weather = get_weather(mode, location, units)
        except KeyError:
            location = wrong_city(location)
            
    _weather_block(weather,
    'F°' if units=='imperial' else 'C°',
    'mph' if units=='imperial' else 'm/s')
    save_city(location)

def _weather_block(data, tUnit, wUnit):
    weather = SingleTable(list(map(lambda day: [
        f'\n\n{icons[day["icon"]]}',
        _weather_data(day, tUnit, wUnit)
    ], data)))
    weather.inner_column_border = False
    weather.inner_row_border = True
    print(weather.table)

def _weather_data(data, tUnit, wUnit):
    return f'\n{c("Location:")} {data["city"]}\n'+ \
    f'{c("Date:")} {data["date"].strftime("%d %b %Y")}\n' + \
    f'{c("Time: ")} {data["date"].strftime("%H:%M")}\n' + \
    f'{data["description"]}\n' + \
    f'{c("Temperature: ")} {data["temp"]}{tUnit}\n' + \
    f'{c("Maximum temperature:")} {data["maxTemp"]}{tUnit}\n' + \
    f'{c("Minimum temperature:")} {data["minTemp"]}{tUnit}\n' + \
    f'{c("Wind")} {_wind_direction(float(data["wind"]["deg"]))} {data["wind"]["speed"]}{wUnit}'

def _wind_direction(wind):
    if wind > 338 or wind < 22: return 'N'
    if wind < 67: return 'NE'
    if wind < 113: return 'E'
    if wind < 157: return 'SE'
    if wind < 202: return 'S'
    if wind < 247: return 'SW'
    if wind < 292: return 'W'
    return 'NW'