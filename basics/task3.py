# Task 1

# data = input('Введите имя, фамилию и возраст через пробел:\n').split()
# name = data[0]
# surname = data[1].lower().title()
# age = data[2]

# name = name.replace('a', '').lower().title()
# surname = '*'.join(surname)

# print((name + surname) * int(age))

# Task 2 

# string = input('Введите строку: ').lower()

# a = string.count('a')
# o = string.count('o')
# i = string.count('i')
# e = string.count('e')
# u = string.count('u')
# y = string.count('y')

# t = string.count('a') + string.count('o') + string.count('i')

# print(f'В вашей строке насчитано {t} гласных букв')

# Task 3

# username = input('Введите юзернейм: ')
# middle = int(len(username) / 2)
# password = (username[:middle] + '&' + username[middle:] + '$').swapcase()
# print(f'Вам сгенерирован пароль:{password}')

# string = input()
# print(string[1::2])

# string = input()
# print(string[:5] + 'K' + string[6:])

string = input()
print(string.replace(string[5], 'K', 6))









