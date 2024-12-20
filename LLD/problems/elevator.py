from enum import Enum
from queue import PriorityQueue

# Direction Enum
class Direction(Enum):
    UP = 1
    DOWN = 2

# ElevatorState Enum
class ElevatorState(Enum):
    MOVING = 1
    IDLE = 2

# Floor Class
class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.external_dispatcher = ExternalDispatcher()

    def press_button(self, direction):
        self.external_dispatcher.submit_external_request(self.floor_number, direction)

# Building Class
class Building:
    def __init__(self, floors):
        self.floor_list = floors

    def add_floor(self, new_floor):
        self.floor_list.append(new_floor)

    def remove_floor(self, remove_floor):
        self.floor_list.remove(remove_floor)

    def get_all_floors(self):
        return self.floor_list

# ElevatorDisplay Class
class ElevatorDisplay:
    def __init__(self):
        self.floor = 0
        self.direction = Direction.UP

    def set_display(self, floor, direction):
        self.floor = floor
        self.direction = direction

    def show_display(self):
        print(f"Floor: {self.floor}, Direction: {self.direction.name}")

# ElevatorCar Class
class ElevatorCar:
    def __init__(self, car_id):
        self.id = car_id
        self.display = ElevatorDisplay()
        self.internal_buttons = InternalButtons()
        self.elevator_state = ElevatorState.IDLE
        self.current_floor = 0
        self.elevator_direction = Direction.UP
        self.elevator_door = "Closed"  # Simplified as a string

    def show_display(self):
        self.display.show_display()

    def press_button(self, destination):
        self.internal_buttons.press_button(destination, self)

    def set_display(self):
        self.display.set_display(self.current_floor, self.elevator_direction)

    def move_elevator(self, direction, destination_floor):
        start_floor = self.current_floor
        if direction == Direction.UP:
            for floor in range(start_floor, destination_floor + 1):
                self.current_floor = floor
                self.set_display()
                self.show_display()
                if floor == destination_floor:
                    return True
        elif direction == Direction.DOWN:
            for floor in range(start_floor, destination_floor - 1, -1):
                self.current_floor = floor
                self.set_display()
                self.show_display()
                if floor == destination_floor:
                    return True
        return False

# ElevatorController Class
class ElevatorController:
    def __init__(self, elevator_car):
        self.up_min_pq = PriorityQueue()
        self.down_max_pq = PriorityQueue()
        self.elevator_car = elevator_car

    def submit_external_request(self, floor, direction):
        if direction == Direction.DOWN:
            self.down_max_pq.put(-floor)  # Negative for max priority
        else:
            self.up_min_pq.put(floor)

    def submit_internal_request(self, floor):
        pass  # Logic to handle internal requests

    def control_elevator(self):
        while True:
            if self.elevator_car.elevator_direction == Direction.UP:
                while not self.up_min_pq.empty():
                    destination = self.up_min_pq.get()
                    self.elevator_car.move_elevator(Direction.UP, destination)

            elif self.elevator_car.elevator_direction == Direction.DOWN:
                while not self.down_max_pq.empty():
                    destination = -self.down_max_pq.get()
                    self.elevator_car.move_elevator(Direction.DOWN, destination)

# ElevatorCreator Class
class ElevatorCreator:
    elevator_controller_list = []

    @staticmethod
    def initialize_elevators():
        elevator_car1 = ElevatorCar(1)
        controller1 = ElevatorController(elevator_car1)

        elevator_car2 = ElevatorCar(2)
        controller2 = ElevatorController(elevator_car2)

        ElevatorCreator.elevator_controller_list.append(controller1)
        ElevatorCreator.elevator_controller_list.append(controller2)

# InternalButtons Class
class InternalButtons:
    def __init__(self):
        self.dispatcher = InternalDispatcher()
        self.available_buttons = list(range(1, 11))  # Example floors 1-10

    def press_button(self, destination, elevator_car):
        if destination in self.available_buttons:
            self.dispatcher.submit_internal_request(destination, elevator_car)

# InternalDispatcher Class
class InternalDispatcher:
    def __init__(self):
        self.elevator_controller_list = ElevatorCreator.elevator_controller_list

    def submit_internal_request(self, floor, elevator_car):
        pass  # Logic to assign internal requests

# ExternalDispatcher Class
class ExternalDispatcher:
    def __init__(self):
        self.elevator_controller_list = ElevatorCreator.elevator_controller_list

    def submit_external_request(self, floor, direction):
        for controller in self.elevator_controller_list:
            elevator_id = controller.elevator_car.id
            if (elevator_id % 2 == 1 and floor % 2 == 1) or (elevator_id % 2 == 0 and floor % 2 == 0):
                controller.submit_external_request(floor, direction)

# Main Execution
if __name__ == "__main__":
    ElevatorCreator.initialize_elevators()

    floor_list = [Floor(i) for i in range(1, 6)]
    building = Building(floor_list)

    # Example: Press button on floor 3 for UP direction
    floor_list[2].press_button(Direction.UP)
