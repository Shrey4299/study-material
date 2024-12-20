from abc import ABC, abstractmethod

# Base Component
class BasePizza(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass

# Concrete Components
class VegDelight(BasePizza):
    def cost(self) -> int:
        return 120

class Margherita(BasePizza):
    def cost(self) -> int:
        return 100

# Decorator Base Class
class ToppingDecorator(BasePizza):
    def __init__(self, pizza: BasePizza):
        self._pizza = pizza

# Concrete Decorators
class ExtraCheese(ToppingDecorator):
    def cost(self) -> int:
        return self._pizza.cost() + 30  # Additional cost for extra cheese

class Olives(ToppingDecorator):
    def cost(self) -> int:
        return self._pizza.cost() + 20  # Additional cost for olives

class Pepperoni(ToppingDecorator):
    def cost(self) -> int:
        return self._pizza.cost() + 25  # Additional cost for pepperoni

# Client code
if __name__ == "__main__":
    # Create a VegDelight pizza
    pizza = VegDelight()
    print(f"Cost of VegDelight Pizza: {pizza.cost()}")

    # Add extra cheese
    pizza_with_extra_cheese = ExtraCheese(pizza)
    print(f"Cost of VegDelight Pizza with Extra Cheese: {pizza_with_extra_cheese.cost()}")

    # Add olives
    pizza_with_olives = Olives(pizza_with_extra_cheese)
    print(f"Cost of VegDelight Pizza with Extra Cheese and Olives: {pizza_with_olives.cost()}")

    # Create a Margherita pizza with pepperoni
    margherita = Margherita()
    pizza_with_pepperoni = Pepperoni(margherita)
    print(f"Cost of Margherita Pizza with Pepperoni: {pizza_with_pepperoni.cost()}")