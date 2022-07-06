"=========== Полиморфизм ============="
# Полиморфизм - это принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разный функционал)

class Dog:
    def speak(self):
        print('гав-гав')

class Cat:
    def speak(self):
        print('мяу-мяу')

class Frog:
    def speak(self):
        print('ква-ква')

animals = [Cat(), Dog(), Cat(), Frog(), Frog()]

for animal in animals:
    animal.speak()

print(dir(str))
print(dir(list))
print(dir(dict))
"=========== Полиморфизм ============="
# Полиморфизм - это принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разный функционал)

class Dog:
    def speak(self):
        print('гав-гав')

class Cat:
    def speak(self):
        print('мяу-мяу')

class Frog:
    def speak(self):
        print('ква-ква')

animals = [Cat(), Dog(), Cat(), Frog(), Frog()]

for animal in animals:
    animal.speak()

print(dir(str))
print(dir(list))
print(dir(dict))
"=========== Полиморфизм ============="
# Полиморфизм - это принцип ООП, в котором методы в разных классах называются одинаково. (один интерфейс - разный функционал)

class Dog:
    def speak(self):
        print('гав-гав')

class Cat:
    def speak(self):
        print('мяу-мяу')

class Frog:
    def speak(self):
        print('ква-ква')

animals = [Cat(), Dog(), Cat(), Frog(), Frog()]

for animal in animals:
    animal.speak()

print(dir(str))
print(dir(list))
print(dir(dict))
print(dir(int))
"a" + "b" == "ab"
[1,2,3] + [4,5,6] == [1,2,3,4,5,6]
{"a":2} + {"b":4} == {"a":2, "b":4}
4 + 6 == 10