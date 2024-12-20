from abc import ABC, abstractmethod

# Abstract Product Classes
class Bike(ABC):
    @abstractmethod
    def assemble(self):
        pass


class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass


# Concrete Product Classes
class SportsBike(Bike):
    def assemble(self):
        return "Assembling a Sports Bike"


class CruiserBike(Bike):
    def assemble(self):
        return "Assembling a Cruiser Bike"


class SportsCar(Car):
    def assemble(self):
        return "Assembling a Sports Car"


class SUVCar(Car):
    def assemble(self):
        return "Assembling an SUV Car"


# Abstract Factory Class
class VehicleFactory(ABC):
    @abstractmethod
    def create_bike(self) -> Bike:
        pass

    @abstractmethod
    def create_car(self) -> Car:
        pass


# Concrete Factories
class SportsVehicleFactory(VehicleFactory):
    def create_bike(self) -> Bike:
        return SportsBike()

    def create_car(self) -> Car:
        return SportsCar()


class FamilyVehicleFactory(VehicleFactory):
    def create_bike(self) -> Bike:
        return CruiserBike()

    def create_car(self) -> Car:
        return SUVCar()


# Client Code
def client_code(factory: VehicleFactory):
    bike = factory.create_bike()
    car = factory.create_car()
    print(bike.assemble())
    print(car.assemble())


# Example usage
if __name__ == "__main__":
    print("Using SportsVehicleFactory:")
    sports_factory = SportsVehicleFactory()
    client_code(sports_factory)

    print("\nUsing FamilyVehicleFactory:")
    family_factory = FamilyVehicleFactory()
    client_code(family_factory)
