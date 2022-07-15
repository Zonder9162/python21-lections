from views import Views
from models import Cars

auto1 = Cars(brand='Ford', model='mustang', year=1985, engine_volume=15, color='black', body_type='хэтчбек', mileage=2000, price=5000)
auto2 = Cars(brand='Deo', model='matiz', year=2005, engine_volume=85,color='black', body_type='купе', mileage=2500, price=4000)

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

