# class Animal:  
#     def speak(self):  
#         print("Animal Speaking")  
# #child class Dog inherits the base class Animal  
# class Dog(Animal):  
#     def bark(self):  
#         print("dog barking")  

# class German(Dog):

#     def bite(self): 
#         print("German bites")

# class Cat(Animal):

#     def meow(self):
#         print("Cat meows")

# d = Dog()  
# d.bark()  
# d.speak()  

# g = German() 
# g.bite() 
# g.bark()


class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  

print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  

print(issubclass(Derived,Calculation2))  
print(issubclass(Calculation1,Calculation2))   
print(isinstance(d,Derived)) 


# **************************************************** Method Overiding ********************************

class Bank:  
    def getroi(self):  
        return 10;  
class SBI(Bank):  
    def getroi(self):  
        return 7;  
  
class ICICI(Bank):  
    def getroi(self):  
        return 8;  
b1 = Bank()  
b2 = SBI()  
b3 = ICICI()  
print("Bank Rate of interest:",b1.getroi());  
print("SBI Rate of interest:",b2.getroi());  
print("ICICI Rate of interest:",b3.getroi());  


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        return f"{self.name} makes a sound"
    
    def nothing(self):
        print("Nothing")

class Dog(Animal):
    def __init__(self, name, color, breed):
        # Call the __init__ method of the parent class (Animal)
        super().__init__(name, color)
        self.breed = breed

    def speak(self):
        # Call the speak method of the parent class (Animal)
        parent_speech = super().speak()
        return f"{parent_speech} and barks"
    
    def detail(self):
        return f"Name: {self.name}, Color: {self.color}, Breed: {self.breed}"

# Usage
dog = Dog("Buddy", "red", "Golden Retriever")
print(dog.speak())  # Output: Buddy makes a sound and barks
print(dog.name)
print(dog.detail()) # Output:
dog.nothing() # Output:


class Shape:
    def area(self):
        pass  # This is a placeholder, to be overridden by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Area of a circle: πr^2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Area of a rectangle: width * height

# Usage
shapes = [Circle(5), Rectangle(4, 6)]

