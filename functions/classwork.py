# def  get_type(a, b):
#     print(type(a))
#     print(type(b))
#     return
# get_type(1, 'hello')

# dict_ = {'1':'Hello', '2':'World'}
# def dictionary(a):
#         for key in a:
#             print(key)
# dictionary(dict_)

# num = 6
# def check(num):
#     if num % 2 == 0:
#         return "It is even number"
#     elif num % 2 != 0:
#         return "It is odd number"
# print(check(num)) 


# def is_palindrome(string):
#     if string == string[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome('goodbey')) 

# def max_num(a, b):
#     if a > b:
#         r a
#     elif a < b:
#         reverse b
# print(max_num(1, 2))

# def multiply_list(a):
#     b = 1
#     for i in a:
#         b *= i
#     return b
# print(multiply_list([1, 2, 3, 4, 5, 6])) 

# def sum_digits(a):
#     b = 0
#     for i in list(str(a)):
#         b += int(i)
#     return b
# print(sum_digits(105)) 

# def generate_password(param1, param2):
#     import random
#     random_list = random.sample(range(1, 10), k = 7)
#     random_list = [str(i) for i in random_list]
#     password = param1 + param2 + ''.join(random_list)
#     return password
# def info(name = input('Введите своё имя: '), surname = input('Введите свою фамилию: ')):
#     password = generate_password(param1 = name, param2 = surname)
#     return password
# print(info())

# def add(a, b):
#     return a + b

# def substract(a, b):
#     return a - b

# def devision(a, b):
#     return a / b

# def multiply(a, b):
#     return a * b

# def get_data(action):
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
    
#     dict_ = {
#         '+':add(num1, num2),
#         '-':substract(num1, num2),
#         '/':devision(num1, num2),
#         '*':multiply(num1, num2)
#     }
#     result = dict_[action]
#     return result

# action = input('Введите один из символов для действия "+","-","/","*": ')
# print(get_data(action))

# def cooking_icecream(name, size, *args):
#     print(f'Ваше {name} мороженное {size} размера')
#     if args:
#         print('Ваши топпинги: ')
#         for i in args:
#             print(i)
# cooking_icecream('шоколадное', 'большого', 'арахис', 'ммеллад')

# def foo():
#     var = 'переменная foo'
  
#     def bar():
#         var = 'переменная bar'
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# number = '1321'
# if int(number[-1]) < int(number[-2]) and int(number[-2])<int(number[-3]):
#     if int(number[-3]) < int(number[-4]):
#         print('YES')
#     else:
#         print('NO')
# else:
#         print('NO')

# number = '4326'
# if int(number[-1]) < int(number[-2]) and int(number[-2])<int(number[-3]) and int(number[-3]) < int(number[-4]):
#         print('YES')
# else:
#         print('NO')

# def foo():
#     global var
#     var = 'переменная foo'
  
#     def bar():
#         global var
#         print('переменная в foo: ', var)
#         var = 'переменная bar'
        
#     bar()
# foo()
# print('переменная в foo: ', var)

# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print(x)
#     x = 'Я могу изменяться'
# my_func()
# print(x)

# num = 3
# def mul():
#     global num
#     num **=2
# mul()
# mul()
# mul()
# print(num)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')
# def pay_bills(amount, log_name):
#     global balance
#     print(f"Вы заплатили {amount} сом за {log_name}")
#     balance -= amount
# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# result = 0
# def pow_first(x,y):
#     global result
#     result = x**y
# def pow_second(z):
#     global result
#     result %= z
# pow_first(2, 3)
# pow_second(3)
# print(result)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control():
#     global a
#     for k, v in a.items():
#         if v >= 17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control')
# age_control()

# a = ['pipi', 'papa', 'mama']
# def registr():
#     global a
#     b = []
#     for i in a:
#         b.append(i.title())
#     print(b)
# registr()

# glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
# sogl = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# num_glas = 0
# num_sogl = 0
# ostolnye = 0

# def count_symbols(string):
#     global glas, sogl, num_glas, num_sogl, ostolnye
#     for i in string.lower():
#         if i in glas:
#             num_glas += 1
#         elif i in sogl:
#             num_sogl += 1
#         else:
#             ostolnye += 1
#     print(f'Количество гласных: {num_glas}, согласных: {num_sogl}, остальных символов: {ostolnye}')

# count_symbols('Мурат супер!')

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def menshe_semi(list_):
#     for i in list_:
#         if i > 7:
#             list_.remove(i)
#     print(list_)
# menshe_semi(a)

# main_matryoshka = 5
# def size():
#     global main_matryoshka
#     medium_matryoshka = 4
#     sum_matryoshka = main_matryoshka +  medium_matryoshka
#     def full_size():
#         nonlocal sum_matryoshka
#         little_matryoshka = 3
#         full_sum_matryoshka = sum_matryoshka + little_matryoshka 
#         print(full_sum_matryoshka)
#     full_size()
# size()

# import math
# class Solution:
#     def mySqrt(x: int):
#         return int(math.sqrt(x))
#     print(mySqrt(8))

#     list_ = [1, 5, -9, 6, -4] 
# result = all(num > 3 for num in list_) 
# print(result)

# list_ = [-1, 0, 45, -24, 78]
# result = any(num < 0 for num in list_)
# print(result)

# list_ = [-1, 0, 45, -24, 78]
# result = any(num < 0 for num in list_)
# print(result)

# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x ** 2, list_)) 
# print(result) 

# list_ = [1, 2, 3, 4]  
# result = list(filter(lambda x: x % 2 == 0, list_)) 
# print(result) 

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda string: len(string)>7, list_)) 
# print(result) 

# import functools 
# list_ = [5, 6, 7, 8] 
# result = functools.reduce(lambda x, y: x * y, list_) 
# print(result) 

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(filter(lambda x: x % 2 == 0,list_)))
# list3 = len(list(filter(lambda x: x % 2 != 0,list_)))
# result = f'even: {list2}, odd: {list3}'
# print(result) 

# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: True if (x > 0) else False, list_))
# print(result)

# import functools 
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = functools.reduce(lambda x, y: x if len(x)>len(y) else y, list_)
# print(result)

# Task 1

# import math

# list_ = [1, 4, 64 , 9, 'Hello world', True, 25, 36, False, 'Python']
# result = list(map(lambda x: round(math.sqrt(x)), filter(lambda y: type(y) == int, list_)))
# print(result)

# Task 2

# dict_ = [
#     {'name' : 'Alfa', 'grade' : 100},
#     {'name' : 'Beta', 'grade' : 80},
#     {'name' : 'Gamma', 'grade' : 40},
#     {'name' : 'Omega', 'grade' : 40}
# ]

# list_of_exclusion = list(filter(lambda x: x['grade'] < 60, dict_))
# names_of_exclusion = list(map(lambda x: x['name'], list_of_exclusion))
# grade_of_exclusion = list(map(lambda x: x['grade'], list_of_exclusion))
# zipped_of_exclusion = list(zip(names_of_exclusion, grade_of_exclusion))

# explusion_list = list(map(lambda x: f'{x[0]}, Вы будете исключены.', zipped_of_exclusion))

# print(explusion_list)

# word_in_list =  ['H', 'l', 'l', 'o', 'w', ' ', 'W', 'o', 'r', 'l', 'd', '!'] 
# import functools 
# complex_word = functools.reduce(lambda x, y: x + y, word_in_list) 
# print(complex_word) 

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {
#     key:
#     2 if value % 2 == 0 else value
#     for key, value in a.items()
# }
# print(b)

list_ = list(range(10000, 100000))
for i in list_:
    if i % 2 == 0:
        i = str(i)
        number = 0
        for j in i:
            number = number+int(j)
        if number%4 == 0:
            if (str(i))[2] in '13579':
                print(i)