# odd_cube
odd_cube_list = []

for i in range(1001):
    odd_cube_list.append(i)

    for digit in odd_cube_list:
        if digit % 2 == 0:
            odd_cube_list.pop()

for i in range(len(odd_cube_list)):
    odd_cube_list[i] = odd_cube_list[i] ** 3

last_digit = 0

for digit_1 in odd_cube_list:
    temporary_list = list(str(digit_1))
    temporary_digit = 0

    for digit_2 in temporary_list:
        temporary_digit += int(digit_2)

    if temporary_digit % 7 == 0:
        last_digit += digit_1

print(last_digit)
# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#   сумма цифр которых делится нацело на 7

for i in range(len(odd_cube_list)):
    odd_cube_list[i] += 17

last_digit = 0

for digit in odd_cube_list:
    temporary_list = list(str(digit))
    temporary_digit = 0

    for digit_2 in temporary_list:
        temporary_digit += int(digit_2)

    if temporary_digit % 7 == 0:
        last_digit += digit
print(last_digit)
