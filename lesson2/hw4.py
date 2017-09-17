# Возьмите словарь с ответами из функции get_answer
# Запишите его содержимое в формате csv в формате: "ключ"; "значение".
# Каждая пара ключ-значение должна располагаться на отдельной строке

import csv

ANSWERS = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Удачи!"}

def dict_to_list(dict):
    list = []
    for element in dict:
        list.append({'question': element,'answer': ANSWERS[element]})
    return list

def csv_write(filename, list):
    with open(filename, 'w', encoding='cp1251') as local_file:
        fields = ['question', 'answer']
        writer = csv.DictWriter(local_file, fields, delimiter = ';', lineterminator="\n")
        writer.writeheader()
        for string in list:
            print(string)
            writer.writerow(string)

output_file_name = 'answers.csv'
csv_write(output_file_name, dict_to_list(ANSWERS))
print('\nРезультат записан в файл {}'.format(output_file_name))