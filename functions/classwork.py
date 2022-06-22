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

def cooking_icecream(name, size, *args):
    print(f'Ваше {name} мороженное {size} размера')
    if args:
        print('Ваши топпинги: ')
        for i in args:
            print(i)
cooking_icecream('шоколадное', 'большого', 'арахис', 'ммеллад')
