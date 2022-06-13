a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Выберите операцию из следующих "+-*/%**//": ')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '**':
    print(a ** b)
elif b != 0:
    if c == '/':
        print(a / b)
    elif c == '%':
        print(a % b)
    elif c == '//':
        print(a // b)
else:
    print('Данной операции нет в системе')