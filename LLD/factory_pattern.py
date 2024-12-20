from abc import ABC, abstractmethod

# Step 1: Create an interface for Shapes
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Step 2: Create concrete classes implementing the Shape interface
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

# Step 3: Create a Factory to generate objects of concrete classes
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Step 4: Client code
if __name__ == "__main__":
    factory = ShapeFactory()

    # Get a Circle
    circle = factory.get_shape("circle")
    print(circle.draw())  # Output: Drawing a Circle

    # Get a Square
    square = factory.get_shape("square")
    print(square.draw())  # Output: Drawing a Square

    # Attempt to get an unknown shape
    try:
        unknown_shape = factory.get_shape("triangle")
    except ValueError as e:
        print(e)  # Output: Unknown shape type: triangle