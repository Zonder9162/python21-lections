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
# a

# from collections import defaultdict

# a = {'a': 1, 'b': 2, 'c': 3} 
# for x, y in list(a.items()):
# print(a)

# a = {'a': 3, 'b': 2}
# print(sum(a.values()))

# a = {'a': 1, 'b': 2, 'c': 1}
# a.items()
# for x, y in list(a.items()): 
#      print(y)

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

# list_ = [1,2,3]
# if list_.count(list_[0]) > 1 or list_.count(list_[1]) > 1:
#     print('yes')
# elif list_.count(list_[2]) > 1:
#     print('yes')
# else:
#     print('ERROR')


# list_ = [n for n in range(1, 50, 2)] 
# print(list_) 

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i % 2 == 0 and i > 0]
# print(int_list)

# list_ = [item ** 2 for item in range(1,26)]
# print(list_)

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list]
# print(int_list)

# list_ = [(i ** 2) if i % 2 == 0 else i for i in range(1, 11)]
# print(list_)

# list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name]
# print(new_list)

# dict_ = {i : i**2 for i in range(1, 11)}
# print(dict_)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# for x, y in a.items(): 
#     y = y / 5
#     a.update[{x : 3}]
# print(a)

# a = {'a': 1, 'b': 2, 'c': 3} 
# for x, y in list(a.items()):
#     a.update({y : x})
#     a.pop(x)
# print(a)

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         b.update({k : 2})
#     else:
#         b.update({k : v})
# print(b)

# a1 = {1 : 'Hello', 2 : 'World'}
# a2 = dict([(1, 2), ('Hello', 'World')])
# a3 = dict.fromkeys(['Hello', 'World'], 1)
# print(a1)
# print(a2)
# print(a3)

# string = "Hello" 
# dict_ = {}
# for i in string:
#     if string.count(i) > 1:
#         dict_.update({i:string.count(i)})
#     else:
#         dict_.update({i:1})

# print(dict_)
# from functools import reduce
# a = {'a': 10, 'b': 9, 'c': 3}
# result = [v for k,v in list(a.items())]
# print(reduce(lambda x, y: x*y, result))

# n = int(input())
# dict_ = {
#     n*i : (n*i)*(n*i)
#     for i in range(1, 501) 
#     if i % i == 0 and n*i <= 500
# }
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {
#     key : list(range(1, value + 1))
#     for key, value in a.items() 
# }
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {
#     key : ('even' if value % 2 == 0 else 'odd')
#     for key, value in dict_.items()
# }
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'.split(' ')
# list_ = [
#     i for i in string_ if i.isdigit()
# ]
# print(list_)

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},

#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
# }
# new_dict = {
#     key : {inner_key for inner_key, inner_value in value.items() if max(inner_value)}
#     for key, value in dict_.items()
# }
# print(max(list(dict_.items())[2][1]))
# print(max(list(dict_.items())[list(dict_).index('Timur')][1]))
# print(new_dict)
# print(max(list(dict_.items())[list(dict_).index('Olga')][2]))
# max(list(dict_.items())[list(dict_).index(key)][1].values())

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# new_dict = {
#     key:
#     list(({inner_key for inner_key, inner_value in value.items() if inner_value == max(list(value.values()))}))[0]
#     for key, value in dict_.items()
#     }
# print(new_dict)


# new_dict = {
#     key : max(list(dict_.items())[1][2])
#     for key, value in dict_.items()
# }
# print(max(list(dict_.items())[0][1]))
# print(max({'history': 90, 'math': 9, 'literature': 91}.values()))

# Task 1

# names = ['Winston', 'Bill', 'Ann', 'Emma']
# letters = ['a', 'o', 'i', 'e', 'y', 'u']

# filter = [name for name in names if name[0].lower() in letters]
# print(filter)

# Task 2

# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# b = {key: {inner_key: inner_value + 2 for inner_key, inner_value in value.items()} for key, value in a.items()}
# print(b)

# Task 3

# list_ = list(range(1, 11))
# set_ = {num ** 2 if num % 2 == 0 else num * 3 for num in list_}
# print(set_)

# input_ = list(input('input : '))
# letters = ['a', 'o', 'i', 'e', 'y', 'u']
# output_ = [len(let) for let in input_ if let in letters]
# print(f'output : {sum(output_)}')

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {
#     key : list({inner_value for inner_key, inner_value in value.items()})[0] for key, value in my_dict.items()
# } 
# print(dict_)

# dict_ = {1 : 'hello', 2 : 'wonderful', 3 : 'world'}
# dict_ = {
#     key : (len(value) if key % 2 == 0 else len(value) ** 3)
#     for key, value in dict_.items()
# }
# print(dict_)

# set1 = [i for i in range(10)]
# set2 = [i for i in range (8,18)]
# ful_set = set1 + set2

# set1 = {i for i in range(10)}
# set2 = {i for i in range(8,18)}
# full_set = set.union(set1,set2)
# num = len(full_set)
# same_letter = len(set.intersection(set1, set2))

# if num < 20:
#     print(f'В этом сете было {same_letter} повторения, его длина составляет {num}')
# else:
#     print("Ваш обьединенный сет полностью уникальный!")

# same_letter = {
    
# }

# print(len(set.intersection(set1, set2)))

# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError
# except ValueError:
#     print('Доступ запрещён')
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except ZeroDivisionError:
#     print('Произошла ошибка!')
# except ValueError:
#     print('Произошла ошибка!')

# inp1 = input()
# inp2 = input()
# try:
#     if int(inp1) != int() or int(inp2) != int():
#         print(inp1 + inp2)
# except:
#     print(int(inp1)) + int(inp2)

# inp1 = input()
# inp2 = input()

# try:
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1 + inp2)

# inp1 = list(input().split(', '))
# list_ = []
# for i in inp1:
#     if int(i) == int():
#         list_.append(i)
#     else:
#         raise Exception('Данный элемент не является числом!')

# dict_ = {1:'Alfa', 2:'Beta', 3:'Gamma'}
# dict_ = {value: key for key, value in dict_.items()}

# try:
#     username = input('Введите имя пользователя: ')
#     ID = dict_[username]
#     print(ID)
# except KeyError:
#     print('В базе данных нет такого пользователя.')
# else:
#     print(f'Добро пожаловать, {username}!')
# finally:
#     print('Спасибо!')

try:
    age = int(input('Введите Ваш возраст: '))
    if age <= 0:
        raise Exception('Ваш возраст должен быть больше 0')
except ValueError:
    print('Введите число, не строку')
else:
    print(f'Ваш возраст: {age}')
    

