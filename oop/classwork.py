# # class Salary:
# #     percent = 8

# #     def __init__(self, salary, experience):
# #         self.salary = salary
# #         self.experience = experience
    
# #     def count_percent(self):
# #         result = (self.salary * self.experience * self.percent) / 100
# #         return result

# # obj = Salary(10000, 10)
# # print(obj.count_percent()) 

# # class Password:
# #     def __init__(self, password):
# #         self.password = password

# #     def validate(self):
# #         if len(self.password) > 8 and len(self.password) < 15:
# #             if self.password.isnumeric:
# #                 if any(map(lambda x: x.isalpha(), self.password)) == True:
# #                     if bool('@#&$%!~*'.find(self.password)):
# #                         return ('Ваш пароль сохранен.')
# #                     else:
# #                         raise Exception('Your password should have some symbols')
# #                 else:
# #                     raise Exception('Password should contain letters as well')        
# #             else:
# #                 raise Exception('Password should contain numbers too') 
# #         else:
# #             raise Exception('Password should be longer than 8, and less than 15')
    
# #     def __str__(self):
# #         return len(self.password)*'*'

# # password = Password('short')
# # print(password.validate())
# # print(password)

# import math

# class Math:
#     def __init__(self, value):
#         self.value = value
    
#     def get_factorial(self):
#         return math.factorial(self.value)
    
#     def get_sum(self):
#         return sum(list(map(int, str(self.value))))
    
#     def get_mul_table(self):
#         result = ''
#         for i in list(range(1,11)):
#             result += f'{self.value}x{i}={self.value * i}\n'
#         return result

# num = Math(11)

# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())


# Task 1

# class Hogwatrs:
    
#     faculties_qualities = {
#         'courage': 'Gryffindor',
#         'intelligence': 'Ravenclaw',
#         'justice': 'Hufflepuff',
#         'ambition': 'Slytherin'
#     }

#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition
#         self.qualities_dictionary = locals()

#     def sorting_hat(self):
#         dictionary = {v: k for k, v in self.qualities_dictionary.items() if type(v) == int()}
#         maximum_point = max(dictionary.keys())
#         maximum_quality = dictionary[maximum_point]
#         self.faculty = Hogwatrs.faculties_qualities[maximum_quality]
#         print(f'{self.faculty}!!!')

# student = Hogwatrs(1,3,7,3)
# student.sorting_hat()

# Task 1

# import random

# class Languages:
#     student_count = 0

#     def __init__(self):
#         Languages.student_count += 1

#     def coding(self):
#         raise NotImplementedError

# class Python(Languages):
#     student_count = 0

#     def __init__(self):
#         Python.student_count += 1
        
#     def __str__(self):
#         return 'Python'

#     def coding(self):
#         print('I am Python student. I am coding now.')

# class JavaScript(Languages):
#     student_count = 0

#     def __init__(self):
#         JavaScript.student_count += 1

#     def __str__(self):
#         return 'JavaScript'

#     def coding(self):
#         print('I am JavaScript student. I am coding now')

# student1 = Python()
# student2 = JavaScript()

# my_choice = input("Guess the student's language: ")
# programm_choice = random.choice([student1, student2])

# programm_choice.coding()

# if programm_choice.__str__() == my_choice:
#     print('Good job!')

# else:
#     print('No bueno :(')

# Task 2

# class MyList(list):
#     def insert(self, arg1, arg2):
#         print('First arg - element, second arg - index')
#         return super().insert(arg2, arg1)

# list1 = MyList([1, 2, 3, 4, 5])
# list1.insert("Makers", 3)
# print(list1)

# Task 1

# class WhatsApp:
#     def __init__(self, phone:int):
#         self.phone = phone

#     def send(self, text:str):
#         print(f'I am sending a text {text}')

# class SnapChat:
#     def __init__(self, phone:int):
#         self.phone = phone

#     def send(self, image:bool, text:str):
#         if image:
#             print(f'I am sending a text {text} with some image')
#         else:
#             print(f'I am sending a text {text} without image')

# class Telegram:
#     def __init__(self, phone:int, username:str):
#         self.phone = phone   
#         self.username = username

#     def send(self, voice_massage:str):
#         print(f'I am sending a voice message {voice_massage}')

# obj1 = WhatsApp(996555666666)
# obj1.send('Hello World!')

# obj2 = SnapChat(996555444444)
# obj2.send(True, 'Hello')

# obj3 = SnapChat(996700888888)
# obj3.send(False, 'Goodbey')

# obj4 = Telegram(996550200775, 'Zonder')
# obj4.send('How are you today?')

# Task 2

# class A:
#     def count(self, word:str):
#         self.count = 0
#         vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#         for letters in word:
#             if letters in vowels:
#                 self.count += 1
#         return self.count

# class B:
#     def count(self, word:str):
#         self.count = 0
#         vowels = ['a', 'o', 'y', 'i', 'e', 'u']
#         for letters in word:
#             if letters not in vowels:
#                 self.count += 1
#         return self.count

# a = A()
# print(a.count('Makers'))
# b = B()
# print(b.count('Makers'))

# Task 

# class Terminal:
#     def _check_card(self, card:str):
#         if len(card) == 16 and card.isdigit():
#             self.__card = card
#         else:
#             print('Invalid card number')

#     def _check_pin(self, pin):
#         if len(pin) == 4 and pin.isdigit():
#             self.pin = pin
#             self.money = 0
#         else:
#             raise Exception('Invalid pin-code')

#     def __init__(self, card, pin):
#         self._check_card(card=card)
#         self._check_pin(pin=pin)
    
#     def _validation(self, pin):
#         if self.__pin == pin:
#             return True
#         else:
#             return False

#     def put(self, pin, money):
#         if self._validation(pin=pin):
#             self.money += money
#             print(f'There is {self.money} on your balance')
#         else:
#             print('Not correct pin-code')
    
#     def _check_money(self, money):
#         if money % 10 == 0:
#             return True
#         else:
#             print('Invalid amount of money')
#             return False

#     def _check_balance(self, money):
#         if self.money < money:
#             print('Not enough money on your balance')
#             return False
#         else:
#             return True

#     def ger_money(self, pin, money):
#         if self._validation(pin=pin):
#             if self._check_money(money=money) and self._check_balance(money=money):
#                 self.money -= money
#                 print(f'There is {self.money} on your balance')
#         else:
#             print('Pin-code is not correct')

# card = Terminal("122435464758", '1234')
# card.put('1234', 1000)
# card.get_money('1234', 900)
# print(card.money)

# Task 1

# from datetime import datetime

# class Smartphone:
#     def call(self, phone_number):
#         print(f'Calling to {phone_number} number')

#     def where_to_wear(self):
#         print('You can keep me anywhere')

# class Watch:
#     def see_time(self):
#         print(f"It's {datetime.now()} now")

# class SmartWatch(Smartphone, Watch):
#     ...

# smartwatch = SmartWatch()
# smartwatch.call('996555666666')
# smartwatch.see_time()

# Task 2

# class CheckMixin:
#     def check(self, username, password):
#         if self.username == username and self.password == password:
#             print("Successfully created!")
#             self.count += 1
#         else:
#             print('Wrong credentials')

# class Instagram(CheckMixin):
#     def __init__(self, username, password):
#         self.username = username 
#         self.password = password
#         self.count = 0

#     def post_post(self, title, username, password):
#         super().check(username=username, password=password)

# class TikTok(CheckMixin):
#     def __init__(self, username, password):
#         self.username = username 
#         self.password = password
#         self.count = 0

#     def post_video(self, video, username, password):
#         super().check(username=username, password=password)

# obj1 = Instagram('Zonder', '123456789')
# obj1.post_post('Test post', 'Zonder', '123456789')
# print(obj1.count)

# obj2 = TikTok('Zonder', '123456789')
# obj2.post_video('Test video', 'Zonder', '123456789')
# print(obj2.count)
            
# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется title {title}')
        
# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')

# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# auto = Auto()
# auto.play_music('Rule Britania')
# boat = Boat()
# boat.play_music('Girls and Panzer')
# obj = Amphibian() 
# obj.play_music('cc')



class Clock:
    def current_time(self):
        import time
        a = time.localtime()
        current_time = time.strftime("%H:%M:%S", a)
        print(current_time)
    
class Alarm:
    def on(self):
       print('Будильник включен')
           
    def off(self):
        print('Будильник выключен')

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        self.on()


clock = AlarmClock()

clock.current_time() 
clock.alarm_on()