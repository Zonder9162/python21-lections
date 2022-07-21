from distutils.log import info


class Cars:
    info = []
    objects = []
    body_types = ['седан', 'универсал', 'купе', 'хэтчбек', 'минивен', 'внедорожник', 'пикап']
    
    def __init__(self, brand:str, model:str, year:int, engine_volume:float, color:str, body_type:str, mileage:int, price:float):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_volume = round(engine_volume, 1)
        self.color = color
        self.mileage = mileage
        self.price = round(price, 2)
        likes = 0
        comment = []

        if body_type in Cars.body_types:
            self.body_type = body_type
        else:
            raise Exception("В выборе отсутствует такой тип кузова")
        Cars.objects.append(self)
        self.id = Cars.objects.index(Cars.objects[-1])
        Cars.info.append({'id':self.id, 'brand':self.brand, 'model':self.model, 'year':self.year, 'engine_volume':self.engine_volume,'body_type':self.body_type, 'color':self.color, 'mileage':self.mileage, 'price':self.price, 'likes':likes, 'comments':comment})