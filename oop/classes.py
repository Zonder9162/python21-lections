"========= OOP ==========="
# OOP - Objext-oriented programming
# ООП - объектно-ориентированнок программирование

from unicodedata import name


class Person:
    name = "Настя"
    age = 12
    arms = 2
    legs = 2

    def walk(arg):
        print(arg)
        print("Я иду")

    def add_age(obj):
        obj.age += 1

# person1 = Person()
# person1.add_age() # Новый вариант
# # Person.add_age() Старый вариант
# print(person1.age)

# Person.age = 17
# print(Person.age)

# person2 = Person()
# print((person2.age))

class Person:
    arms = 2
    legs = 2

    def __init__(self, name, age):
        """
        Функция, которая вызывается, когда мы создаём объект от класса self - ссылка на созданный объект
        """
        self.name = name # мы добавляем в объект self новый аттрибут name
        self.age = age # новый аттрибут age

    def add_age(obj):
        """
        функция, которая принимает обьект и изменяет его возраст на 1
        """
        obj.age += 1

    def __str__(self, name, age):
        """
        Функция кторая вызывается, когда мы оборачиваем объект в класс str или когда принтуем объект 
        Функция ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return f"{self,name} - {self.age} у.о"

person1 = Person("Настя", 50)
print(person1.age)

person2 = Person("Жаркынай", 15)
print(person2.age)

"=========== Атрибуты класса ==========="
# Атрибуты класса - это переменные внутри класса

"============ Методы класса ============="
# Методы класса - это функции внутри класса

"============ Объекты класса ============"
# Объекты, экзэмпляр, instance класса - это объект созданный по шаблону класса (он перенимает все аттрибуты и методы у класса)

"=========== Аттрибуты и методы объекта ============" 
# Аттрибуты и методы, кторые есть у объекта, но возможно их нет у класса

class A:
    var1 = "переменная класса"

    def __init__(self):
        self.var2 = "переменная объекта"

print(dir(A)) 
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']

obj = A()
print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

print(A.var1) #  'переменная класса'
# print(A.var2) # AttributeError: type object 'A' has no attribute 'var2'

print(obj.var1) # 'переменная класса'
print(obj.var2) # 'переменная объекта'

"Класс имеет доступ только к аттрибутам класса"
"Объеткт имеет доступ и к аттрибутам класса, и к его аттрибутам самого объекта"