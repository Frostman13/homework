# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, вывести улицу, на которой больше всего остановок.

import csv
                                
def read_csv(filename):
    list = []
    with open(filename, 'r', encoding='cp1251') as local_file:
        fields = ['ID', 'Name',  'Longitude_WGS84', 'Latitude_WGS84', 'Street','AdmArea' ,'District' ,'RouteNumbers' ,
        'StationName' ,'Direction', 'Pavilion', 'OperatingOrgName','EntryState' ,'global_id' ,'geoData']
        reader = csv.DictReader(local_file, fields, delimiter=';')
        for row in reader:
            list.append(row)
    return list

source_data = read_csv('data_source\data-398-2017-09-14.csv')


# создаём список из улиц, на которых расположены остановки (с дублями)
# streets = []
# for stop in source_data:
#     street_name = stop['Street']
#     streets.append(street_name)
# print(streets)
    
# Вариант 1
max_stops = 0
streets_counter_list = {}
for stop in source_data:
    street_name = stop['Street']
    if streets_counter_list.get(street_name):
        streets_counter_list[street_name] += 1
        if (streets_counter_list[street_name] > max_stops) and (street_name != 'проезд без названия'):
            max_stops = streets_counter_list[street_name]
            max_stops_street = street_name
    else:
        streets_counter_list[street_name] = 1
print('Больше всего остановок: {} - {}'.format(max_stops_street, max_stops))

# Вариант 2
max_stops = 0
streets_counter_list = {}
for stop in source_data:
    street_name = stop['Street']
    streets_counter_list[street_name] = streets_counter_list.get(street_name, 0) + 1
    if (streets_counter_list[street_name] > max_stops) and (street_name != 'проезд без названия'):
        max_stops = streets_counter_list[street_name]
        max_stops_street = street_name
print('Больше всего остановок: {} - {}'.format(max_stops_street, max_stops))



