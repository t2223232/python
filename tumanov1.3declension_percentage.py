# declension_percentage
declension_list = ['процентов', 'процент', 'процента']
percentage = 1
while percentage <= 100:
    if 20 >= percentage >= 10:
        print(percentage, declension_list[0])

    elif percentage % 10 == 1:
        print(percentage, declension_list[1])

    elif 4 >= percentage % 10 >= 2:
        print(percentage, declension_list[2])

    else:
        print(percentage, declension_list[0])
    percentage += 1
