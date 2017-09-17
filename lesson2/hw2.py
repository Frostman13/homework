# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import timedelta, date, time, datetime

now = datetime.now()
now = datetime(2019, 3, 31)

def yesterday(day):
    yesterday = (day-timedelta(1,0,0)).strftime('%d.%m.%y')
    return yesterday

def day_last_month(day):
    if now.month == 1:
        day_last_month = datetime(now.year-1,12,now.day).strftime('%d.%m.%y')
    elif (now.month == 3) and (now.day > 28):
        if now.year % 4 == 0:
            day_last_month = datetime(now.year,2,29).strftime('%d.%m.%y')
        else:
            day_last_month = datetime(now.year,2,28).strftime('%d.%m.%y')
    elif (now.month in (5,7,10)) and (now.day == 31):
        day_last_month = datetime(now.year,now.month-1,30).strftime('%d.%m.%y')
    else:
        day_last_month = datetime(now.year,now.month-1,now.day).strftime('%d.%m.%y')
    return day_last_month

print('Вчера было {}'.format(yesterday(now)))
print('Сегодня {}'.format((now).strftime('%d.%m.%y')))
print('Месяц назад было {}'.format(day_last_month(now)))
print(datetime.strptime('01/01/17 12:10:03.234567','%d/%m/%y %H:%M:%S.%f'))
