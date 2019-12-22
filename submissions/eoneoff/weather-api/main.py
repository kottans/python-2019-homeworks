import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--location')
parser.add_argument('-r', '--range', default='day')
parser.add_argument('-u', '--units', default='celsius')

args=parser.parse_args()

mode = 'forecast' if args.range == 'week' else 'weather'
units = 'imperial' if args.units == 'farenheit' else 'metric'