import ephem
from datetime import datetime
PLANETS = ['Mercury', 'Venus','Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

# Определение созвездия
def get_constellation_name(planet_name):
    planet_name = planet_name.capitalize()
    if planet_name in PLANETS:
        planet = getattr(ephem, planet_name)
        result = ephem.constellation(planet(datetime.now()))[1]
    else:
        result = 'Нет такой планеты'
    return result

planet_name = input('Введите название планеты на английском:\n')
print('Планета {} в созвездии {}'.format(planet_name,get_constellation_name(planet_name)))

# Добавлено в tg_bot