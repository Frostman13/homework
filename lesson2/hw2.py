# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import timedelta, date, time, datetime
    
print('Вчера было {}'.format((datetime.now()-timedelta(1,0,0)).strftime('%d.%m.%y')))
print('Сегодня {}'.format((datetime.now()).strftime('%d.%m.%y')))
print('Месяц назад было {}'.format(datetime(datetime.now().year,datetime.now().month-1,datetime.now().day).strftime('%d.%m.%y')))
print(datetime.strptime('01/01/17 12:10:03.234567','%d/%m/%y %H:%M:%S.%f'))
