class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    print(f"Area of the shape: {shape.area()}")

rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(4, 6)

calculate_area(rectangle)  
calculate_area(circle)     
calculate_area(triangle)  
