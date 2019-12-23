from manage_cities import read_recent, read_favourite

def wrong_city(city):
    print(f'here is no weather data for the city with the name {city}' if city \
        else 'There is no city name provided')
    print('''1. Select city form recent
2. Select city from favourite
3. Enter city
0. Cancel''')
    choice = get_choice(3)
    if choice == '1':
        return select_recent()
    elif choice == '2':
        return select_favourite()
    elif choice == '3':
        return input('Enter city name: ')
    else: exit(0)

def select_recent():
    recent = read_recent()
    for i in range(len(recent)):
        print(f'{i+1}. {recent[i]}')
    print('0. Cancel')
    choice = get_choice(len(recent))
    if choice == '0': return ''
    else: return recent[int(choice)-1]

def select_favourite():
    favourite = [name for name in read_favourite().keys()]
    for i in range(len(favourite)):
        print(f'{i+1}. {favourite[i]}')
    print('0. Cancel')
    choice = get_choice(len(favourite))
    if choice == '0': return ''
    else: return favourite[int(choice)-1]

def get_choice(number):
    choice = ''
    while not choice.isdigit() or int(choice) not in range(number+1):
        choice = input(f'Select {", ".join(map(str, range(1, number+1)))} or 0: ')
    return choice