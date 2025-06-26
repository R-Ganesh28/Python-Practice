#Basic Class and Object(Constructors)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Hello, This is {self.name}. My age is {self.age}.")
        
p1 = Person('John', 36)
p1.display()
