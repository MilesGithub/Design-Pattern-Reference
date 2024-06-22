from abc import ABC, abstractmethod

def main():
    # Applying different strategies to prepare pizza based on crust type
    thin_crust_strategy = ThinCrustStrategy()
    pizza_order = PizzaOrder(thin_crust_strategy)
    print("Preparing pizza with Thin crust:")
    pizza_order.prepare_pizza()

    print("\n")

    thick_crust_strategy = ThickCrustStrategy()
    pizza_order.set_crust_strategy(thick_crust_strategy)
    print("Preparing pizza with Thick crust:")
    pizza_order.prepare_pizza()

    print("\n")

    stuffed_crust_strategy = StuffedCrustStrategy()
    pizza_order.set_crust_strategy(stuffed_crust_strategy)
    print("Preparing pizza with Stuffed crust:")
    pizza_order.prepare_pizza()
    

# Strategy interface for crust preparation
class CrustStrategy(ABC):
    @abstractmethod
    def prepare_crust(self):
        """Prepare the crust based on the type."""
        pass

# Concrete strategy for Thin crust
class ThinCrustStrategy(CrustStrategy):
    def prepare_crust(self):
        print("Rolling the dough thin and baking quickly.")

# Concrete strategy for Thick crust
class ThickCrustStrategy(CrustStrategy):
    def prepare_crust(self):
        print("Rolling the dough thick and baking at a moderate temperature.")

# Concrete strategy for Stuffed crust
class StuffedCrustStrategy(CrustStrategy):
    def prepare_crust(self):
        print("Stuffing the edges with cheese before baking.")


# Context class utilizing a strategy to prepare pizza
class PizzaOrder:
    def __init__(self, crust_strategy: CrustStrategy):
        self.crust_strategy = crust_strategy

    def set_crust_strategy(self, crust_strategy: CrustStrategy):
        self.crust_strategy = crust_strategy

    def prepare_pizza(self):
        self.crust_strategy.prepare_crust()
        self.add_toppings()
        self.bake()
        self.cut()
        self.box()

    def add_toppings(self):
        print("Adding toppings: tomato sauce, mozzarella cheese, and pepperoni slices.")

    def bake(self):
        print("Baking the pizza at 375 degrees Fahrenheit.")

    def cut(self):
        print("Cutting the pizza into slices.")

    def box(self):
        print("Placing the pizza in a box.")

if __name__ == "__main__":
    main()
