# Остановки у метро
# Объединить наборы данных из предыдущих задач и посчитать,
# у какой станции метро больше всего остановок (в радиусе 0.5 км).
import csv
import json
from geopy.distance import vincenty

def read_csv(filename):
    list = []
    with open(filename, 'r', encoding='cp1251') as local_file:
        fields = ['ID', 'Name',  'Longitude_WGS84', 'Latitude_WGS84', 'Street','AdmArea' ,'District' ,'RouteNumbers' ,
        'StationName' ,'Direction', 'Pavilion', 'OperatingOrgName','EntryState' ,'global_id' ,'geoData']
        reader = csv.DictReader(local_file, fields, delimiter=';')
        next(reader)
        for row in reader:
            list.append(row)
    return list

source_stops_data = read_csv('data_source\data-398-2017-09-14.csv')

with open('data_source\data-397-2017-09-06.json') as local_file:
    source_metro_data = json.load(local_file)

stations_list = {}
max_stops_counter = 0

for station in source_metro_data:
    station_name = station['NameOfStation']
    if stations_list.get(station_name) == None:
        stations_list[station_name] = station['geoData']

for station in stations_list:
    station_geodata = (stations_list.get(station)['coordinates'][0],stations_list.get(station)['coordinates'][1])    
    stops_counter = 0
    for stop in source_stops_data:
        stop_geodata = (stop['Longitude_WGS84'], stop['Latitude_WGS84'])
        if vincenty(station_geodata, stop_geodata).meters <= 500:
            stops_counter += 1
    if stops_counter >= max_stops_counter:
        max_stops_counter = stops_counter
        station_max_stops = station
print('Больше всего остановок, {}, у станции "{}"'.format(max_stops_counter, station_max_stops))



# Расчёт для примера
# print(source_stops_data[1]['Longitude_WGS84'])
# print(source_stops_data[1]['Latitude_WGS84'])
# print('\n')
# print(source_metro_data[1]['Longitude_WGS84'])
# print(source_metro_data[1]['Latitude_WGS84'])

# point_a = (source_stops_data[1]['Longitude_WGS84'],source_stops_data[1]['Latitude_WGS84'])
# point_b = (source_metro_data[1]['Longitude_WGS84'],source_metro_data[1]['Latitude_WGS84'])
# print(vincenty(point_a, point_b).meters)
