import random
name = input('Введите вше имя: ')
guess_number = 0
choice = input(f'{name} не хотите ли поиграть в "Угадай число"? Напишите "да" или "нет": ')
random_number = random.randint(1, 10)
if choice == 'да':
    print('Число загадано')
    guess = -1
    while guess != random_number:
        guess = int(input('Введите число: '))
        if guess == random_number:
            continue_ = input(f'Поздравляю {name}! Вы угадали загаданное число, количество попыток равно {guess_number}.Хотите поиграть ещё раз? Напишите "да" или "нет": ')
            if continue_ == 'да':
                continue
            elif continue_ == 'нет':
                break
        elif guess != random_number:
            continue
        guess_number = guess_number + 1
elif choice == 'нет':
    print('Хорошо, нет так нет')
print('До свидания!')

