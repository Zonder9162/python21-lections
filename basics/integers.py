"======================ПЕРЕМЕННЫЕ======================="
# переменные - это ссылки на ячейки памяти, где хранятся какие-то данные
a = 5

"========================Ввод и вывод данных===================="
# print -это функция вывода данных в терминал
# input - это функция ввода данных с терминала 
# b = input()
# print ("веденное число", a, b)

"=============Числа=========="
# integers(int) - wtkst xbckf (1, 2, 3, 4 ...)
# float - вещественные (с плавующей точкой) (0.3, 0.45, 7.49)
# demical - точное вещественное число
# чтобы исп. decimal нужно его импортировать 
from decimal import Decimal
c = Decimal(0.1) 
# complex - комплексные числа
complex(1, 5)

"==========Операции над числами============="
# 5 + 5 - сложение
# 10 - 4 вычитание
#  2 * 5 умножение
# 15 / 3 деление (float 5.0) 
# 15 // 2 целочисленное деление (int 7)
# 5 ** 2 возведение в степень 
# 25 ** 0.5 квадратный корень числа 
# 5 % 2 остаток от деления (int 1)

# модуль числа - делает число из отрицательного в положительное |-5| = 5
# abs(-5) (int 5)
# abs(10)(int 10)

# pow:
# 1. возводит число в определённую степень
# 2. озвращает остаток от деления результата 1 действия на третье число
# pow(2, 3) 8 = 2 ** 3
# pow(2, 3, 4) 8 % 4 = 0
# (2 ** 3) % 4 = 0

# divmod - функция, кторая принимает 2 числа и возвращает 2 числа, где первое - это целая часть от деления, а второе - остаток от деления
# divmod(9, 3) 3, 0
# divmod(15, 2) 7, 1

# round - функция, которая округляет число 
# round(5.6) 6
# round (3.5) 4
# round(4.4) 4
# round(5.49) берёт первок число после точки 
# можно указать сколько цифр после запятой оставить 
round (10.0475, 3) # 10.048
round (10.0474, 3) # 10.047

# scrt - функция для нахождения корня из числа
# для работы нужно её импортировать из библиотеки math 
from math import scrt
scrt(36) # 6
scrt(25) # 5
print()