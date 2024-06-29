class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        """Method untuk mendeskripsikan restoran"""
        description = f"{self.name} is a {self.cuisine_type} restaurant."
        return description

    def open_restaurant(self):
        """Method untuk menandakan restoran dibuka"""
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        """Method untuk mengatur jumlah pelanggan yang dilayani"""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Method untuk menambahkan jumlah pelanggan yang dilayani"""
        self.number_served += additional_customers

restaurant1 = Restaurant("Ristorante Italiano", "Italian")

print(restaurant1.describe_restaurant())  
restaurant1.open_restaurant()  

restaurant1.set_number_served(50)
print(f"Number of customers served: {restaurant1.number_served}") 
restaurant1.increment_number_served(30)
print(f"Updated number of customers served: {restaurant1.number_served}")  
