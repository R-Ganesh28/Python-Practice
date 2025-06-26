#Inheritance
class Animal:
    def Sound(self):
        print("bark")
        
class Cat(Animal):
    def Sound(self):
        print("meow")
        
A = Animal()
A = Cat()
A.Sound()

#Encapsulation
class Student:
    def __init__(self):
        self.__marks = 90
        
    def set_marks(self, m):
        self.__marks = m
        
    def get_marks(self):
        print(self.__marks)
        
S1 = Student()
S1.get_marks()

#Polymorphism
class dog:
    def info(self):
        print("This is a dog.")
        
class Cat:
    def info(self):
        print("this is a Cat.")
        
for Animal in (dog(), Cat()):
    Animal.info()
    
