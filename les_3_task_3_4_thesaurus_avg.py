# Задание №3
"""
def thesaurus(args):
    tez_key = list(set(s[:1].title() for s in args))
    tez = {}
    for itm in tez_key:
        tez_val = (list(filter(lambda x: x[:1].title() == itm.title(), args)))
        tez.update({itm: tez_val})
    return tez
"""


# Задание №4
def thesaurus_avg(args):
    tez_tot = {}
    tez = list(set(((s.split(' ')[1])[:1]).title() for s in args))
    for itm in tez:
        tez_val = (list(filter(lambda x: ((x.split(' ')[1])[:1]).title() == itm.title(), args)))
        tez2 = list(set(((s.split(' ')[0])[:1]).title() for s in tez_val))
        for itm2 in tez2:
            tez_val2 = (list(filter(lambda x: ((x.split(' ')[0])[:1]).title() == itm2.title(), tez_val)))
            tez_tot.update({itm: {itm2: tez_val2}})
    return tez_tot


# m = (input('Ввести Имена:')).split(', ')
n = (input('Ввести Имена Фамилиии:')).split(', ')
print(n)
# print(m)
print(thesaurus_avg(n))
# print(thesaurus(m))
