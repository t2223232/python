list_cost = [45.67, 73.00, 43, 26.74, 23.7, 43.54, 768.07, 332, 78.00, 21.7]
str_res = ''

for itm in list_cost:
    _item = ('%d руб' % itm, "%.2d коп" % ((itm - int(itm)) * 100))
    _item2 = ' '.join(_item)
    if itm == list_cost[-1]:
        str_res = str_res + _item2
    else:
        str_res = str_res + _item2 + ', '
        print(str_res)

print(list_cost, 'id list', id(list_cost))
list_cost.sort()
print(list_cost, 'id list', id(list_cost))
list_cost_reverse = list_cost[::-1]
print(list_cost_reverse)
print(list_cost[::-1])  # без создания нового списка
print(list_cost_reverse[0:5])
print(list_cost[::-1][0:5])  # без создания нового списка
