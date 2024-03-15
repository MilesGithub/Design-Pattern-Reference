from abc import ABC, abstractmethod

def main():
    print("Order from store 1")
    store_1 = PizzaStore1()  # Initialize and order from Pizza Store 1
    store_1.order_pizza()

    print("\nOrder from store 2")
    store_2 = PizzaStore2()  # Initialize and order from Pizza Store 2
    store_2.order_pizza()

# Abstract Creator
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self) -> 'Pizza':
        pass  # Factory method to be implemented by subclasses

    def order_pizza(self) -> None:
        pizza = self.create_pizza()  # Instantiate the pizza
        # Following the pizza preparation process
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

# Concrete Creators
class PizzaStore1(PizzaStore):
    def create_pizza(self) -> 'Pizza':
        return MargheritaPizza()  # Create a Margherita Pizza

class PizzaStore2(PizzaStore):
    def create_pizza(self) -> 'Pizza':
        return PepperoniPizza()  # Create a Pepperoni Pizza

# Abstract Product
class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> None:
        pass  # Prepare the pizza

    @abstractmethod
    def bake(self) -> None:
        pass  # Bake the pizza

    @abstractmethod
    def cut(self) -> None:
        pass  # Cut the pizza

    @abstractmethod
    def box(self) -> None:
        pass  # Box the pizza

# Concrete Products
class MargheritaPizza(Pizza):
    def prepare(self) -> None:
        print("Preparing Margherita Pizza")

    def bake(self) -> None:
        print("Baking Margherita Pizza")

    def cut(self) -> None:
        print("Cutting Margherita Pizza")

    def box(self) -> None:
        print("Boxing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self) -> None:
        print("Preparing Pepperoni Pizza")

    def bake(self) -> None:
        print("Baking Pepperoni Pizza")

    def cut(self) -> None:
        print("Cutting Pepperoni Pizza")

    def box(self) -> None:
        print("Boxing Pepperoni Pizza")

if __name__ == "__main__":
    main()
