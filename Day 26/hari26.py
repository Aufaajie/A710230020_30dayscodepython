class Restaurant:
    def __init__(self, name, cuisine_type, rating=0):
        self._name = name
        self._cuisine_type = cuisine_type
        self._rating = rating
        self._number_of_customers_served = 0

    @property
    def name(self):
        return self._name

    @property
    def cuisine_type(self):
        return self._cuisine_type

    @property
    def rating(self):
        return self._rating

    @property
    def number_of_customers_served(self):
        return self._number_of_customers_served

    def set_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self._rating = new_rating
            print(f"Rating set to {self._rating}")
        else:
            print("Rating should be between 0 and 5.")

    def increment_customers_served(self, num_customers):
        if num_customers > 0:
            self._number_of_customers_served += num_customers
            print(f"{num_customers} customers served. Total served: {self._number_of_customers_served}")
        else:
            print("Number of customers should be greater than zero.")

restaurant1 = Restaurant("Italiano's", "Italian")

print(f"Restaurant Name: {restaurant1.name}")
print(f"Cuisine Type: {restaurant1.cuisine_type}")
print(f"Rating: {restaurant1.rating}")
print(f"Number of Customers Served: {restaurant1.number_of_customers_served}")

restaurant1.set_rating(4.5)
restaurant1.increment_customers_served(50)

print(f"Updated Rating: {restaurant1.rating}")
print(f"Updated Number of Customers Served: {restaurant1.number_of_customers_served}")
