# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

# Задаём переменные
school_score_sum = 0
school_score_count = 0
school_results = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [5,3,4,3,5]},
{'school_class': '4c', 'scores': [4,4,4,3,5]},{'school_class': '4d', 'scores': [3,2,5,3,4]}]

for class_number in school_results:
    class_score_sum = sum(class_number['scores'])
    class_score_count = len(class_number['scores'])
    avg_class_score = class_score_sum / class_score_count
    school_score_sum += class_score_sum
    school_score_count += class_score_count
    print('Средний результат по классу {}: {}'.format(class_number['school_class'],round(avg_class_score,2)))
avg_school_score = school_score_sum / school_score_count
print('Средний результат по школе: {}'.format(round(avg_school_score,2)))
