def save_city(city):
    save_recent(city)
    save_favourite(city)

def save_recent(city):
    recent = read_recent()
    if city in recent: return
    recent.insert(0, city)
    write_recent(recent[0:10])

def save_favourite(city):
    favourite = read_favourite()
    count = favourite.setdefault(city, 0)
    favourite[city]=count+1
    write_favourite({k:v for k,v in sorted(favourite.items(), key=lambda c: c[1], reverse=True)[0:10]})

def read_recent():
    try:
        with open('recent.csv', 'r') as f:
            return f.read().splitlines()
    except:
        return []

def write_recent(recent):
    with open('recent.csv', 'w') as f:
        f.writelines(map(lambda c: f'{c}\n', recent))

def read_favourite():
    try:
        with open('favourite.csv', 'r') as f:
            return {name: int(count) for name, count in [city.split(';') for city in f.read().splitlines()]}
    except:
        return {}

def write_favourite(favourite):
    with open('favourite.csv', 'w') as f:
        f.writelines([f'{name};{count}\n' for name,count in favourite.items()])