import urllib.request
import argparse
from collections import Counter

apikey = '2ae04d95d78eb539f7b8cce05a16f9e5'


def top():
    line_list = [this_line.rstrip('\n') for this_line in open('Locations.txt')]
    l_sorted = Counter(line_list).most_common()
    try:
        print('Most popular queries:')
        print(l_sorted[0][0])
        print(l_sorted[1][0])
        print(l_sorted[2][0])
        print('What query do you like?')
        by_location(input())
    except IndexError:
        pass
    exit()


def by_location(city_name):
    if city_name[0:4] == 'lat=':
        q = 'http://api.openweathermap.org/data/2.5/forecast?' + city_name + '&APPID=' + apikey
    else:
        q = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city_name + '&APPID=' + apikey
    try:
        fp = urllib.request.urlopen(q)
        mybytes = fp.read()
        mystr = mybytes.decode('utf8')
        fp.close()
    except urllib.error.HTTPError:
        print('Wrong city or cords!!!')
        exit()
    if mystr == '{"cod": 500,"message": "Internal server error"}':
        print('Wrong city or cords!')
        exit()
    else:
        decode(mystr)
        f = open('Locations.txt', 'a+')
        f.write(city_name + '\n')
        f.close()
        exit()


def last_city(number):
    try:
        with open('Locations.txt', 'r') as f:
            lines = f.read().splitlines()
            line = lines[-int(number):-1]
            line.append(lines[-1])
            return line
    except IndexError:
        print('Please enter the location')


def decode(page):
    new_data = page.split('"')
    pa = [i for i, x in enumerate(new_data) if x == 'temp']
    if args.range == 'day':
        print("Temp = " + translate((new_data[pa[8] + 1]).strip(':,')))
    else:
        print("Temp = " + translate((new_data[pa[39] + 1]).strip(':,')))


def translate(temperature):
    if not args.degrees:
        new_temperature = float(temperature) - 273.15
    else:
        new_temperature = float(temperature) * 9 / 5 - 459.67
    return str(format(new_temperature, '.2f'))


parser = argparse.ArgumentParser(description='Weather app #37462189')
subparsers = parser.add_subparsers()
parser.add_argument('--l', '-location', dest='location', default=None, type=str, help='Location by city')
parser.add_argument('--r', '-range', dest='range', choices=('day', 'week'), default='day',
                    type=str, help='Range (week/day)')
parser.add_argument('--c', '-cords', nargs=2, dest='cords', type=str,
                    help='Location by coordinates, 2 floats, lon&lat')
parser.add_argument('--d', '-celsius', action='store_false', default=False, dest='degrees',
                    help='Show Celsius degrees (default)')  # false
parser.add_argument('--f', '-fahrenheit', action='store_true', default=False, dest='degrees',
                    help='Show  Fahrenheit degrees')
parser.add_argument('--q', '-resent', dest='resent',
                    help='Show  N resent towns, or 0 for all locations')
parser_top = subparsers.add_parser('top', help='list of 3 favorite cities')
parser_top.set_defaults(func=top)
args = parser.parse_args()
try:
    args.func()
except AttributeError:
    pass
if args.resent is not None:
    print(last_city(args.resent))
if args.cords is not None:
    by_location('lat=' + args.cords[0] + '&lon=' + args.cords[1])
if args.location is not None:
    by_location(args.location)
if (args.cords is None) and (args.location is None) and (args.resent is None):
    last = (str(last_city(1)[0]))
    print(last)
    by_location(last)
