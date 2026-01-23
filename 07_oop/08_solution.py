class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model
    
my_car = Car("Tata", "Safari")
print(my_car.model)