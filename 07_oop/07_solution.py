class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "Car are means of transport"
    
my_car = Car("Tata", "Safari")    
print(my_car.general_description())