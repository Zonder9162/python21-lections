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

# for x in range(1, 101):
#     if (x % (3 * 5)) == 0:
#         print('FizzBuzz') 
#     elif (x % 3) == 0:
#         print('Fizz')
#     elif (x % 5) == 0:
#         print('Buzz')
#     else: 
#         print(x)

# a = int(input('Введите число: '))

# if a > 0:
#     print(f'Число {a} - положительное')
# elif a < 0:
#     print(f'Число {a} - отрицательное')
# else: 
#     print(f'Число {a} - это 0')

# x = int(input())
# y = int(input())
# chastnoe = int(x // y)
# ostatok = x % y
# if ostatok == 0:
#     print('x делится на y')
#     print(f'Частное: {chastnoe}')
# else:
#     print('x не делится на н')
#     print(f'Частное: {chastnoe}')
#     print(f'Остаток: {ostatok}')

# year = int(input())
# if year % 400 == 0:
#     print('YES')
# elif year % 4 == 0:
#     if year % 100 > 0 or year % 100 < 0:
#         print('YES')
#     else: 
#         print('NO')  
# else: 
#     print('NO')

# Task 1

# password = input()

# if password.isdigit() and len(password) >= 8:
#     print('Ваш пароль сохранен')
# elif not password.isdigit():
#     print('Ваш пароль должен хранить только числа')
#     if len(password) < 8:
#         print('Ваш пароль должен содержать не менее 8 символов')

# Task 2

# grades = input('Введите свои баллы по математике, английскому языку и литературе через запятую:\n').split(', ')

# mathematics = int(grades[0])
# english = int(grades[1])
# literature = int(grades [2])

# gpa = (mathematics + english + literature) / 3

# if gpa > 69:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {round(gpa, 1)}')
# else:
#     print(f'Вы не допущенны к экзаменамю Ваш средний бал состовляет {round(gpa, 1)}')

# Task 3

# import random
# game_choices = ['Камень', 'Ножницы', 'Бумага']

# my_choice = input('Ваш выбор: ')
# computer_choice = random.choice(game_choices)
# print(f'Выбор комьпютера: {computer_choice}')

# if my_choice == 'Камень' and computer_choice == 'Камень':
#     print('Ничья.')
# if my_choice == 'Камень' and computer_choice == 'Ножницы':
#     print('Вы выиграли!')
# if my_choice == 'Камень' and computer_choice == 'Бумага':
#     print('Вы проиграли')
# if my_choice == 'Ножницы' and computer_choice == 'Камень':
#     print('Вы проиграли')
# if my_choice == 'Ножницы' and computer_choice == 'Ножницы':
#     print('Ничья.')
# if my_choice == 'Ножницы' and computer_choice == 'Бумага':
#     print('Вы выиграли!')
# if my_choice == 'Бумага' and computer_choice == 'Камень':
#     print('Вы выиграли!')
# if my_choice == 'Бумага' and computer_choice == 'Ножницы':
#     print('Вы проиграли.')
# if my_choice == 'Бумага' and computer_choice == 'Бумага':
#     print('Ничья.')

# Task 11
string.digit 
string.punctuation