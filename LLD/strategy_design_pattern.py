from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface
class DrivingStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass


# Step 2: Implement Concrete Strategies
class NormalDriveStrategy(DrivingStrategy):
    def drive(self):
        return "Driving at normal speed."


class AggressiveDriveStrategy(DrivingStrategy):
    def drive(self):
        return "Driving aggressively at high speed!"


class HeavyLoadDriveStrategy(DrivingStrategy):
    def drive(self):
        return "Driving carefully with heavy load."


class EcoDriveStrategy(DrivingStrategy):
    def drive(self):
        return "Driving in eco mode to save fuel."


# Step 3: Define the Context Class (Vehicle)
class Vehicle:
    def __init__(self, name: str, strategy: DrivingStrategy):
        self.name = name
        self.strategy = strategy

    def set_strategy(self, strategy: DrivingStrategy):
        """Change the driving strategy dynamically."""
        self.strategy = strategy

    def drive(self):
        """Perform driving based on the selected strategy."""
        print(f"{self.name}: {self.strategy.drive()}")


# Step 4: Use the Strategy Pattern in Action
if __name__ == "__main__":
    # Assign initial strategies
    bike = Vehicle("Bike", NormalDriveStrategy())
    truck = Vehicle("Truck", HeavyLoadDriveStrategy())
    sports_car = Vehicle("Sports Car", AggressiveDriveStrategy())

    # Vehicles driving with their initial strategies
    bike.drive()         # Normal driving
    truck.drive()        # Heavy load driving
    sports_car.drive()   # Aggressive driving

    print("\nChanging strategies dynamically...")

    # Dynamically change driving strategy
    bike.set_strategy(EcoDriveStrategy())  # Bike switches to eco mode
    truck.set_strategy(NormalDriveStrategy())  # Truck switches to normal mode
    sports_car.set_strategy(EcoDriveStrategy())  # Sports car switches to eco mode

    # Vehicles driving with their updated strategies
    bike.drive()
    truck.drive()
    sports_car.drive()
