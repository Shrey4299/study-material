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



from typing import Final, final

# Example of Final for variables and attributes
MY_CONSTANT: Final = 42

class Example:
    MAX_SIZE: Final = 100

# Example of Final for methods
class Animal:
    @final
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    # Uncommenting the following method will raise an error if type checked with mypy or similar tools
    # def speak(self):
    #     print("Dog barks")
    pass

# Example of Final for classes
@final
class AnimalClass:
    pass

# Uncommenting the following class will raise an error if type checked with mypy or similar tools
# class DogClass(AnimalClass):
#     pass

# Usage examples
def main():
    print(f"MY_CONSTANT: {MY_CONSTANT}")
    print(f"Example.MAX_SIZE: {Example.MAX_SIZE}")

    # Demonstrating usage of the Animal and Dog classes
    animal = Animal()
    animal.speak()  # Output: Animal sound

    dog = Dog()
    # dog.speak()  # Uncommenting this will cause an error if type checked with mypy or similar tools

    # Uncomment the following to see the error for inheriting from a final class
    # dog_class = DogClass()  # Error if type checked with mypy or similar tools

if __name__ == "__main__":
    main()


