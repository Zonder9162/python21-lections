from models import Cars

class Views:
    
    def create():
        brand_ = str(input('Впишите марку: '))
        model_ = str(input('Впишите модель: '))
        year_ = int(input('Впишите год выпуска: '))
        engine_volume_ = round(float(input('Впишите объем двигателя: ')), 1)
        color_ = str(input('Впишите цвет: '))
        body_type_ = str(input('Впишите тип кузова: '))
        mileage_ = int(input('Впишите пробег: '))
        price_ = round(float(input('Впишите цену: ')), 2)

        Cars(brand=brand_, model=model_, year=year_, engine_volume=engine_volume_, color=color_, body_type=body_type_, mileage=mileage_, price=price_)

    def listing():
        for i in Cars.info:     
            print('\n'.join((
                "========================\n"
                f"ID - {i['id']}",
                f"Марка - {i['brand']}",
                f"Модель - {i['model']}",
                f"Год выпуска- {i['year']}",
                f"Обьем двигателя - {i['engine_volume']}",
                f"Цвет - {i['color']}",
                f"Тип кузова - {i['body_type']}",
                f"Пробег - {i['mileage']}",
                f"Цена - {i['price']}",
                f"Лайки - {i['likes']}",
                f"Комментарии - {i['comments']}\n",
            )))

    def retrieve():
        num = int(input('Введите ID автомобиля для просмотра: '))
        list_ = []   
        for i in Cars.info:
            list_.append(i['id'])
        if num in list_:
            for i in Cars.info:            
                if num == i['id']:
                    print('\n'.join((
                        "========================\n"
                        f"ID - {i['id']}",
                        f"Марка - {i['brand']}",
                        f"Модель - {i['model']}",
                        f"Год выпуска- {i['year']}",
                        f"Обьем двигателя - {i['engine_volume']}",
                        f"Цвет - {i['color']}",
                        f"Тип кузова - {i['body_type']}",
                        f"Пробег - {i['mileage']}",
                        f"Цена - {i['price']}",
                        f"Лайки - {i['likes']}",
                        f"Комментарии - {i['comments']}\n",
                    )))
        else: 
            print('В базе данных нет такого ID')

    def update():
        num_choice_auto = int(input('Введите ID автомобиля для изменения параметров: '))
        list_ = []
        for i in Cars.info:
            list_.append(i['id'])
        if num_choice_auto in list_:
            num_choice_param = int(input('Для того, чтобы изменит параметры описания выберите цифру:\nМарка - 1\nМодель - 2\nГод выпуска - 3\nОбъем двигателя - 4\nЦвет - 5\nТип кузова - 6\nПробег - 7\nЦена - 8\n'))
            print(num_choice_param == 1)
            if num_choice_param in [1, 2, 3, 4, 5, 6, 7, 8]:
                if num_choice_param == 1:
                    Cars.info[num_choice_auto]['brand'] = str(input('Впишите марку: '))
                elif num_choice_param == 2:
                    Cars.info[num_choice_auto]['model'] = str(input('Впишите модель: '))
                elif num_choice_param == 3:
                    Cars.info[num_choice_auto]['year'] = int(input('Впишите год выпуска: '))
                elif num_choice_param == 4:
                    Cars.info[num_choice_auto]['engine_volume'] = round(float(input('Впишите объем двигателя: ')), 1)
                elif num_choice_param == 5:
                    Cars.info[num_choice_auto]['color'] =  str(input('Впишите цвет: '))
                elif num_choice_param == 6:
                    Cars.info[num_choice_auto]['body_type'] = str(input('Впишите тип кузова: '))
                elif num_choice_param == 7:
                    Cars.info[num_choice_auto]['mileage'] = int(input('Впишите пробег: '))
                elif num_choice_param == 8:
                    Cars.info[num_choice_auto]['price'] = round(float(input('Впишите цену: ')), 2)
            else:
                print('Команда под таким номером не существует')
        else:
            print('В базе данных нет такого ID')

    def delete():
        num = int(input('Введите ID автомобиля для удаления: '))
        list_ = []
        for i in Cars.info:
            list_.append(i['id'])
        if num in list_:
            Cars.info.pop(num)
        else:
            print('В базе данных нет такого ID')

    def like():
        num_choice_auto = int(input('Введите ID автомобиля для того чтобы поставить лайк: '))
        list_ = []
        for i in Cars.info:
            list_.append(i['id'])
        if num_choice_auto in list_:
            answer = input('Поставить лайк?(Y,N)\n')
            if answer == 'Y':
                Cars.info[num_choice_auto]['likes'] += 1
                print('Лайк поставлен')
            elif answer == 'N':
                print('Лайк не поставлен')
        else:
            print('В базе данных нет такого ID')
    
    def comment():
        num_choice_auto = int(input('Введите ID автомобиля для того чтобы написать комментарий: '))
        list_ = []
        for i in Cars.info:
            list_.append(i['id'])
        if num_choice_auto in list_:
            name = str(input('Введите своё имя: '))
            comment = str(input('Напишите комментарий: '))
            Cars.info[num_choice_auto]['comments'].append(f'{name}: {comment}')
        else:
            print('В базе данных нет такого ID')