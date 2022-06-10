# Task 1

# day = input('Введите свой день рождения: ')
# month = input('Введите свой месяц рождения: ')
# year = input('Введите свой год рождения: ')

# birthday = print(int(day) + int(month) + int(year)) 

# Task 2

# cost_of_education = 600
# sale = int(input('Введите скидку: '))
# result = cost_of_education - (cost_of_education * sale / 100)

# cost_with_sale = print('Итоговая цена состовляет', result)

# Task 3

# from math import pi
# r = int(input('Введите радиус круга: '))
# area = pi * r**2
# lenght = 2 * pi * r

# print('Площадь круга составляет', round(area, 2))
# print('Длина круга составляет', round(lenght, 2))

# for x in range(1, 101): 
#     if x % 3 == 0:
#         print('Fizz')
#     if x % 5 == 0:
#         print('Buzz')
#     if x % (3 * 5) == 0:
#         print('FizzBuzz') 
#     else: 
#         print(x)

for x in range(1, 101):
    if (x % (3 * 5)) == 0:
        print('FizzBuzz') 
    elif (x % 3) == 0:
        print('Fizz')
    elif (x % 5) == 0:
        print('Buzz')
    else: 
        print(x)

# a = int(input('Введите число: '))

# if a > 0:
#     print(f'Число {a} - положительное')
# elif a < 0:
#     print(f'Число {a} - отрицательное')
# else: 
#     print(f'Число {a} - это 0')

