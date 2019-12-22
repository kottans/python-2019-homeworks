from get_weather import get_weather
from icons import icons

def show_weather(mode, location, units):
    print(get_weather(mode, location, units))