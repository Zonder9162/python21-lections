from views import Views
from models import Cars

auto1 = Cars('Ford', 'mustang', 1985, 15, 'black', 'хэтчбек', 2000, 5000)
auto2 = Cars('Deo', 'matiz', 2005, 85, 'black', 'купе', 2500, 4000)

while True:
    choice = int(input('Добро пожаловать в Автосалон!\nВыберите действие:\nСоздать запись - 1\nПолучить список записей - 2 \nПолучить конкретную запись - 3\nРедактировать/обновить запись - 4\nУдалить запись - 5\nПоставить лайк - 6\nНаписать комментарий - 7\n'))
    if choice in [1, 2, 3, 4, 5, 6, 7]:
        if choice == 1:
            Views.create()
        elif choice == 2:
            Views.listing()
        elif choice == 3:
            Views.retrieve()
        elif choice == 4:
            Views.update()
        elif choice == 5:
            Views.delete()
        elif choice == 6:
            Views.like()
        elif choice == 7:
            Views.comment()

