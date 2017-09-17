# В этом задании требуется определить, на каких станциях московского метро сейчас идёт ремонт эскалаторов и
#  вывести на экран их названия.
# Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539.

import json

with open('data_source\data-397-2017-09-06.json') as local_file:
    source_data = json.load(local_file)

stations_list = {}

for station in source_data:
    station_name = station['NameOfStation']
    if station['RepairOfEscalators']:
        if stations_list.get(station_name) == None:
            stations_list[station_name] = station['RepairOfEscalators'][0]['RepairOfEscalators']

print(stations_list)
