class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class Car(Vehicle):
    def __init__(self, seats, **kwargs):
        super().__init__(**kwargs)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, engineCC, **kwargs):
        super().__init__(**kwargs)
        self.engineCC = engineCC
        
car = Car(6, brand="BMW", model="SUV")
bike = Bike(200, brand="Harley Davidsons", model="Royal Enfield")

print(f"Car Specs----\nModel: {car.model}, Brand: {car.brand}, {car.seats} Seats are available")

print(f"Bike Specs----\nModel: {bike.model}, Brand: {bike.brand}, {bike.engineCC}CC Powerful Engine.")