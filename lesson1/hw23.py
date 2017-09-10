# Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера".
# Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.

# Задаём переменные
NAMES = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(search_name):
    find_status = 'Не найден'
    while len(NAMES) > 0:
        name = NAMES.pop()
        # print(name)
        if name == search_name:
            find_status = 'Нашёлся!'
            break
    return find_status

print(NAMES)
print('Валера: {}'.format(find_person('Валера')))
