class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
safariTwo = Car("Tata", "Fortunar")
print(Car.total_car)
