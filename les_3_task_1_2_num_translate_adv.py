digits_in_eng = input('Enter your number in english:')
DIGIT_LIST = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

# Задание №1
'''
def num_translate(number):
    if number in DIGIT_LIST:
        return DIGIT_LIST[number]
    return None
'''


# Задание №2
def num_translate_adv(args):
    if args.lower() in DIGIT_LIST:
        if args.istitle():
            return DIGIT_LIST[args.lower()].title()
        return DIGIT_LIST[args]
    return None


print(num_translate_adv(digits_in_eng))
