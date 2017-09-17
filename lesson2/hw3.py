# Скачайте файл по ссылке
# Прочитайте его и подсчитайте количество слов в тексте

# Импортируем регулярные выражения
import re

# Задаём переменные для подсчёта
words_number = 0

with open('referat.txt', 'r', encoding = 'utf-8') as work_file:
    content = work_file.read()
    # заменяем символ переноса строки и двойные пробелы на пробел
    content = re.sub(r'\s+', ' ', content)
    # находим символы: не буквы и не цифры
    non_letter_char = re.findall('\W', content)    
    for symbol in non_letter_char:
        # if symbol not in [' ', '\n']:
        # можно записать проще, так как строка и так проверяется посимвольно
        if symbol not in ' \n':
            content = content.replace(symbol,'')
    for symbol in content:
        if symbol == " ":
            words_number +=1
    print('В тексте {} сл.'.format(words_number))