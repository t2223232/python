list_lab = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for item in list_lab:
    _list_lab = item.split(' ')
    _list_lab.reverse()
    name = _list_lab[0].title()
    exit_str = 'Привет, {}!'.format(name)
    print(exit_str)
