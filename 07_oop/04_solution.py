# 4. Encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"  

my_tesla = Car("Tesla", "Model S")
print(my_tesla.get_brand())       
