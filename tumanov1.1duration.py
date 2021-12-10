# duration
duration = int(input('Введите временной промежуток в секундах:'))
day = duration // 86400
hour = duration % 86400 // 3600
minutes = duration % 3600 // 60
seconds = duration % 3600 % 60

if day > 0:
    print(day, 'дн ', hour, 'час ', minutes, 'мин ', seconds, 'сек')
elif hour > 0:
    print(hour, 'час ', minutes, 'мин ', seconds, 'сек')
elif minutes > 0:
    print(minutes, 'мин ', seconds, 'сек')
else:
    print(seconds, 'сек')
