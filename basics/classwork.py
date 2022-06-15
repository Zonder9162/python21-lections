# # Task 1

# # day = input('Введите свой день рождения: ')
# # month = input('Введите свой месяц рождения: ')
# # year = input('Введите свой год рождения: ')

# # birthday = print(int(day) + int(month) + int(year)) 

# # Task 2

# # cost_of_education = 600
# # sale = int(input('Введите скидку: '))
# # result = cost_of_education - (cost_of_education * sale / 100)

# # cost_with_sale = print('Итоговая цена состовляет', result)

# # Task 3

# # from math import pi
# # r = int(input('Введите радиус круга: '))
# # area = pi * r**2
# # lenght = 2 * pi * r

# # print('Площадь круга составляет', round(area, 2))
# # print('Длина круга составляет', round(lenght, 2))

# # for x in range(1, 101): 
# #     if x % 3 == 0:
# #         print('Fizz')
# #     if x % 5 == 0:
# #         print('Buzz')
# #     if x % (3 * 5) == 0:
# #         print('FizzBuzz') 
# #     else: 
# #         print(x)

# # for x in range(1, 101):
# #     if (x % (3 * 5)) == 0:
# #         print('FizzBuzz') 
# #     elif (x % 3) == 0:
# #         print('Fizz')
# #     elif (x % 5) == 0:
# #         print('Buzz')
# #     else: 
# #         print(x)

# # a = int(input('Введите число: '))

# # if a > 0:
# #     print(f'Число {a} - положительное')
# # elif a < 0:
# #     print(f'Число {a} - отрицательное')
# # else: 
# #     print(f'Число {a} - это 0')

# # x = int(input())
# # y = int(input())
# # chastnoe = int(x // y)
# # ostatok = x % y
# # if ostatok == 0:
# #     print('x делится на y')
# #     print(f'Частное: {chastnoe}')
# # else:
# #     print('x не делится на н')
# #     print(f'Частное: {chastnoe}')
# #     print(f'Остаток: {ostatok}')

# # year = int(input())
# # if year % 400 == 0:
# #     print('YES')
# # elif year % 4 == 0:
# #     if year % 100 > 0 or year % 100 < 0:
# #         print('YES')
# #     else: 
# #         print('NO')  
# # else: 
# #     print('NO')

# # Task 1

# # password = input()

# # if password.isdigit() and len(password) >= 8:
# #     print('Ваш пароль сохранен')
# # elif not password.isdigit():
# #     print('Ваш пароль должен хранить только числа')
# #     if len(password) < 8:
# #         print('Ваш пароль должен содержать не менее 8 символов')

# # Task 2

# # grades = input('Введите свои баллы по математике, английскому языку и литературе через запятую:\n').split(', ')

# # mathematics = int(grades[0])
# # english = int(grades[1])
# # literature = int(grades [2])

# # gpa = (mathematics + english + literature) / 3

# # if gpa > 69:
# #     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {round(gpa, 1)}')
# # else:
# #     print(f'Вы не допущенны к экзаменамю Ваш средний бал состовляет {round(gpa, 1)}')

# # Task 3

# # import random
# # game_choices = ['Камень', 'Ножницы', 'Бумага']

# # my_choice = input('Ваш выбор: ')
# # computer_choice = random.choice(game_choices)
# # print(f'Выбор комьпютера: {computer_choice}')

# # if my_choice == 'Камень' and computer_choice == 'Камень':
# #     print('Ничья.')
# # if my_choice == 'Камень' and computer_choice == 'Ножницы':
# #     print('Вы выиграли!')
# # if my_choice == 'Камень' and computer_choice == 'Бумага':
# #     print('Вы проиграли')
# # if my_choice == 'Ножницы' and computer_choice == 'Камень':
# #     print('Вы проиграли')
# # if my_choice == 'Ножницы' and computer_choice == 'Ножницы':
# #     print('Ничья.')
# # if my_choice == 'Ножницы' and computer_choice == 'Бумага':
# #     print('Вы выиграли!')
# # if my_choice == 'Бумага' and computer_choice == 'Камень':
# #     print('Вы выиграли!')
# # if my_choice == 'Бумага' and computer_choice == 'Ножницы':
# #     print('Вы проиграли.')
# # if my_choice == 'Бумага' and computer_choice == 'Бумага':
# #     print('Ничья.')

# # Task 11
# string.digit 
# string.punctuation

# Task 1

# university = {
#     'программирование':100,
#     'экономика':200,
#     'медицина':300
# }

# university['программирование'] = 125
# print(university)

# university['лингвистика'] = 150
# print(university)

# university.pop('медицина')
# print(university)

# print(sum(list(university.values())))

# Task 2

# dictionary = {1: 'a', 2: 'b', 3: 'c'}
# dictionary1 = {}
# for key, val in dictionary.items():
#     dictionary1.update({val:key})
# print(dictionary1) 

# Task 3

# count = int(input('Как много гостей Вы хотите пригласить? '))
# guests = {}
# for x in range(1, count + 1):
#     guest_name = input('Назовите имя гостя: ')
#     guests.setdefault(x, guest_name)
# print(guests)

# Task 4

# product_list = {
#     'чипсы':60,
#     'сардины':30,
#     'сахар':15
# }

# while product_list:
#     remove_product = input()
#     if remove_product in product_list:
#         del product_list[remove_product]
#         print(product_list)
# print('Все продукты из списка уже в корзине, подойдите к кассе за покупкой.')

# a = {'x': 1, 'y': 2, 'z': 1}
# print(a.keys()) 

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.clear()
# print(b)

# Калькулятор

# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys()))

# a = {'a': 1, 'b': 2, 'c': 1}
# a.items()
# for x, y in a: 
#      print(x, y)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for k, v in list(a.items()):
#     if v == None:
#         del a[k]   
# print(a)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# for x, y in list(a.items()):
#     a[y] = y / 5
# print(a)

# from collections import defaultdict

# a = {'a': 1, 'b': 2, 'c': 3} 
# for x, y in list(a.items()):
# print(a)

# a = {'a': 3, 'b': 2}
# print(sum(a.values()))

# Task 1

# str_numbers = input('Введите цифры через запятую: ').split(', ')
# int_numbers = []
# for number in str_numbers:
#     int_numbers.append(int(number))
# print(int_numbers[0], int_numbers[-1])
# str_numbers.pop()
# str_numbers.append('makers')
# print(str_numbers)

# Task 2
# import random
# numbers = random.sample(range(0, 10), k = 10)
# print(numbers)
# print(sorted(numbers))

# Task 3 
# list_ = input('Введите слова через запятую: ').split(', ')
# numbers = []
# for words in list_:
#     numbers.append(int(len(words)))
# print(list_)
# print(numbers)

# name_of_friends = ['Альфа', 'Бета', 'Омега', 'Гамма']
# while name_of_friends:
#     print(name_of_friends[0])
#     del name_of_friends[0]

# name_of_list = ['Helloworld!']

# half_length = int((len(name_of_list[0])) // 2)

# chast1 = name_of_list[0][:half_length]

# chast2 = name_of_list[0][half_length:]

# if int(len(name_of_list[0])) % 2 != 0:
#     half_length = int(len(chast1)) + 1

# new_chast1 = name_of_list[0][0:half_length]

# new_chast2 = name_of_list[0][half_length:]

# new_list = new_chast2 + new_chast1

# print(list(new_list))
   
# labels = ['Honda', 'Kawasaki']
# for i in labels:
#     print(f'I like brand {i}')

# list_ = ['world', 'hello'] 
# list_.reverse()
# new_list = list_
# print(new_list)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = list(filter(lambda x: x < 5, nums))
# print(res)

# x = input().split(', ')
# list_ = list(x)
# tuple_ = tuple(x)
# print(list_)
# print(tuple_)

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)

# list_ = [1, 1, 3]
# for i in list_:
#     if list_.count(i) < 1:
#         x = 'ERROR'
#     else:
#         y = 'yes'
# if list_.count(random(list_)) > 0:
#     print('yes')
# else:
#     print('ERROR')

# x = list(range(84, 9184))
# list_ = []
# for i in x:
#     if i % 5 == 0:
#         list_.append(i)
# print(list_)

list_ = [1,2,3]
if list_.count(list_[0]) > 1 or list_.count(list_[1]) > 1:
    print('yes')
elif list_.count(list_[2]) > 1:
    print('yes')
else:
    print('ERROR')


    

