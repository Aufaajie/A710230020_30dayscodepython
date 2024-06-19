class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def display_info(self):
        return f"Brand: {self.brand}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def display_info(self):
        return f"Car - Brand: {self.brand}, Model: {self.model}, Year: {self.year}"

class ElectricCar(Car):
    def __init__(self, brand, year, model, battery_capacity):
        super().__init__(brand, year, model)
        self.battery_capacity = battery_capacity
    
    def display_info(self):
        return f"Electric Car - Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Battery Capacity: {self.battery_capacity} kWh"

vehicle = Vehicle("Toyota", 2020)
print(vehicle.display_info())

car = Car("Ford", 2018, "Fiesta")
print(car.display_info())

electric_car = ElectricCar("Tesla", 2022, "Model S", 100)
print(electric_car.display_info())
