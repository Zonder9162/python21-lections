"============== Class, static, instanse methods =============="
# instanse метод (метод объекта) - метод, который принимает первым аргументом self (объект). Вызываем instanse методы у объекта.

class A:
    def instanse_method(self):
        print('метод объекта')

obj_a = A()
obj_a.instanse_method() # вызываем у объекта, и он автоматически попадает как аргумент в метод
A.instanse_method(obj_a) # вызываем у класса, нужно передать объект

# class method (метод объекта) - метод, который принимает первым аргументом cls (класс), чтобы создать метод класса, нужно метод задекорировать classmethod.

class A:
    @classmethod
    def class_method(cls):
        print(cls)
        print('Метод класса')

A.class_method()
A().class_method()

class Pizza:

    def __init__(self, radius, *ingridients):
        self.ingridients = ingridients
        self.r = radius

    def cook(self):
        print(f'Пицца размером {self.r} см\nИнгредиенты:\n{self.ingridients}')

    @classmethod
    def pepperoni(cls, r):
        return cls(r, "Пепперони", "Помидоры")

    @classmethod
    def four_cheeze(cls, r):
        return cls(r, "Моцарелла", "Дор блю", "Сыр 3", "Сыр 4")

pizza1 = Pizza(30, "сыр", "помидоры", "грибы")
pizza2 = Pizza.pepperoni(35)
pizza3 = Pizza.pepperoni(25)
pizza4 = Pizza.four_cheeze(30)
pizza5 = Pizza.four_cheeze(35)

pizzas = [pizza1, pizza2, pizza3, pizza4, pizza5]
for pizza in pizzas:
    pizza.cook()


# static method - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом

class Square:
    def __init__(self, a):
        self.a = a 
        self.s = self.get_s()

    @staticmethod
    def get_s(a):
        return a ** 2

obj = Square(4)
print(obj.s)


