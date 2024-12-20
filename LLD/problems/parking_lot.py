from abc import ABC, abstractmethod
from datetime import datetime


# Vehicle Classes
class Vehicle(ABC):
    """Abstract class for vehicles."""
    def __init__(self, license_plate: str):
        self.license_plate = license_plate


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


class Bus(Vehicle):
    pass


# Parking Spot Classes
class ParkingSpot(ABC):
    """Abstract parking spot."""
    def __init__(self, spot_id: str, spot_type: str):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        """Parks a vehicle in the spot."""
        self.is_available = False
        self.vehicle = vehicle

    def remove_vehicle(self):
        """Removes the vehicle from the spot."""
        self.is_available = True
        self.vehicle = None


class CompactSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, "Compact")


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, "Large")


class BikeSpot(ParkingSpot):
    def __init__(self, spot_id: str):
        super().__init__(spot_id, "Bike")


# Parking Floor Class
class ParkingFloor:
    """Represents a floor in the parking lot."""
    def __init__(self, floor_id: str):
        self.floor_id = floor_id
        self.parking_spots = []

    def add_parking_spot(self, spot: ParkingSpot):
        """Adds a parking spot to the floor."""
        self.parking_spots.append(spot)

    def get_available_spots(self, spot_type: str):
        """Returns all available spots of a specific type."""
        return [spot for spot in self.parking_spots if spot.is_available and spot.spot_type == spot_type]


# Parking Ticket Class
class ParkingTicket:
    """Represents a parking ticket."""
    def __init__(self, ticket_id: str, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot = spot
        self.issue_time = datetime.now()
        self.exit_time = None

    def close_ticket(self):
        """Closes the ticket and calculates duration."""
        self.exit_time = datetime.now()
        duration = (self.exit_time - self.issue_time).total_seconds() // 60
        return duration


# Parking Lot Class
class ParkingLot:
    """Represents the parking lot."""
    def __init__(self, name: str):
        self.name = name
        self.floors = {}
        self.tickets = {}

    def add_floor(self, floor: ParkingFloor):
        """Adds a floor to the parking lot."""
        self.floors[floor.floor_id] = floor

    def park_vehicle(self, vehicle: Vehicle, spot_type: str):
        """Parks a vehicle in the first available spot of the required type."""
        for floor in self.floors.values():
            available_spots = floor.get_available_spots(spot_type)
            if available_spots:
                spot = available_spots[0]
                spot.park_vehicle(vehicle)
                ticket = ParkingTicket(f"Ticket-{len(self.tickets) + 1}", vehicle, spot)
                self.tickets[ticket.ticket_id] = ticket
                print(f"Vehicle {vehicle.license_plate} parked at spot {spot.spot_id} on floor {floor.floor_id}.")
                return ticket
        print(f"No available spots for {spot_type} vehicles.")
        return None

    def remove_vehicle(self, ticket_id: str):
        """Removes a vehicle using its ticket."""
        if ticket_id not in self.tickets:
            print("Invalid ticket.")
            return None

        ticket = self.tickets[ticket_id]
        duration = ticket.close_ticket()
        spot = ticket.spot
        spot.remove_vehicle()
        print(f"Vehicle {ticket.vehicle.license_plate} removed from spot {spot.spot_id}. Duration: {duration} minutes.")
        del self.tickets[ticket_id]


# Main Function
if __name__ == "__main__":
    # Create a parking lot
    lot = ParkingLot("Downtown Parking")

    # Add floors
    floor1 = ParkingFloor("Floor1")
    floor2 = ParkingFloor("Floor2")

    lot.add_floor(floor1)
    lot.add_floor(floor2)

    # Add spots to floors
    for i in range(1, 6):
        floor1.add_parking_spot(CompactSpot(f"C1-{i}"))
        floor2.add_parking_spot(LargeSpot(f"L2-{i}"))
        floor2.add_parking_spot(BikeSpot(f"B2-{i}"))

    # Park vehicles
    car1 = Car("CAR123")
    bike1 = Bike("BIKE456")
    ticket1 = lot.park_vehicle(car1, "Compact")  # Parks in Floor1, Compact Spot
    ticket2 = lot.park_vehicle(bike1, "Bike")  # Parks in Floor2, Bike Spot

    # Remove vehicles
    if ticket1:
        lot.remove_vehicle(ticket1.ticket_id)  # Removes the car
    if ticket2:
        lot.remove_vehicle(ticket2.ticket_id)  # Removes the bike
