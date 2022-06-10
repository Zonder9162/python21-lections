"=============Логические операторы==============="
# логические операторы - выражения, которые возвращают True, если правда, False - если ложь

5 == 5 # True
4 == 5 # False

5 != 5 # False
5 != 2 # True

5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False

5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

'5' == 5 # False

"===========Boolean Type==========="
# Булевый тип данных - имеет всего 2 значения True и False
bool(1) # True
bool(0) # False
bool(-277) # False

bool('Hello') # True
bool('') # False
bool(' ') # True

bool(True) # True
bool(False) # False

"==============None Type=============="
# None - тип данных с одним значением  None, который используется для обозначения пустых значений или отсутствия значения
bool(None) # False
bool('None') # True

a = None
print(bool(a)) # False
print(a is None) # True
# is - проверка на полное соответствие

"=========Условные операторы=============="
# Условные операторы нужны для того, чтобы при разных входных данных код работал по разному 

if условие1:
    тело1 
    # будет работать только если условие1 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
else:
    тело2
    # будет работать только если условие1 неверно и условие2 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать только если условие1 неверно и условие2 верно

if условие1:
    тело1
    # будет работать только если условие1 верно
elif условие2:
    тело2
    # будет работать только если условие1 неверно и условие2 верно
else:
    тело3
    # будет работать только если условие1но и условие2 неверно

# в одной конструкции мы можем использовать неограниченное кол-во elif
# в одной конструкции мы можем использовать только 1 if
# else  мы также можем использовать только 1 раз или не использовать вообще

a = int(input('Введите число: '))

if a > 0:
    print(f'Число {a} - положительное')
elif a < 0:
    print(f'Число {a} - отрицательное')
else: 
    print(f'Число {a} - это 0')


 
"==========FizzBuzz========"
"======FizzBuzz======"
# выведите числа от 1 до 100
# если число кратно 3 - вывести Fizz
# если число кратно 5 - вывести Buzz
# если число кратно и 5 и 3 - вывести FizzBuzz
# если число не кратно ни 5 ни 3 - вывести число

# for x in range(1, 101):
#     if (x % (3 * 5)) == 0:
#         print('FizzBuzz') 
#     elif (x % 3) == 0:
#         print('Fizz')
#     elif (x % 5) == 0:
#         print('Buzz')
#     else: 
#         print(x)

# for i in range(1, 17):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

