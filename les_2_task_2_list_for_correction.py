import re

list_old = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(len(list_old))
inx = 0
while inx < len(list_old):
    if re.search('\d+', list_old[inx]) is not None and not list_old[inx].isdigit():
        _item = list_old[inx].zfill(3)
        list_old[inx] = _item
        list_old.insert(inx, '"')
        list_old.insert(inx + 2, '"')
        # print(_item, 'с плюсом', inx)
        # print(list_old)
        inx += 3
    elif list_old[inx].isnumeric():
        _item = "%02d" % int(list_old[inx])
        list_old[inx] = _item
        list_old.insert(inx, '"')
        list_old.insert(inx + 2, '"')
        # print(_item, 'число', inx)
        # print(list_old)
        inx += 3
    # print(inx)
    inx += 1

res = ''
for inx in range(len(list_old)):
    if list_old[inx].isalpha():
        res = res + list_old[inx] + ' '
    elif re.search('\d+', list_old[inx]) is not None:
        res = res + list_old[inx - 1] + list_old[inx] + list_old[inx + 1] + ' '
print(res)
