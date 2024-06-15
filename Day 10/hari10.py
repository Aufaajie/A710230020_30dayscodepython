class Employee:    
    num_of_employees = 0
    raise_amount = 1.05  

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        Employee.num_of_employees += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee("John", "Doe", 50000)
emp2 = Employee("Jane", "Smith", 60000)

print(emp1.full_name())  
print(emp1.salary)       
print(emp2.full_name())  
print(emp2.salary)      
Employee.set_raise_amount(1.07) 
emp1.apply_raise()
emp2.apply_raise()
print(emp1.salary)  
print(emp2.salary)  
print(Employee.num_of_employees)  
