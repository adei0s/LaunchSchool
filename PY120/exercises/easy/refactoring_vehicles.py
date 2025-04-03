class Vehicle:
    def __ini__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels
        
    def info(self):
        return f"{self.make} {self.model}"

class Car:
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle:
    def __init__(self, make, model):
        super().__init__(make,  model, 2)

class Truck:
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload
