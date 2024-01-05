from abc import ABC, abstractmethod

def main():
  
    print("Order from store 1")
    store_1 = Pizza_Store_1()
    store_1.order_pizza()
    print("\n")
    print("Order from store 2")
    store_2 = Pizza_Store_2()
    store_2.order_pizza()

# Creator interface
class Pizza_Store(ABC):
    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass

    def order_pizza(self) -> None:
        pizza = self.create_pizza()

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

# Concrete creator implementations
class Pizza_Store_1(Pizza_Store):
    def create_pizza(self) -> Pizza:
        return Margherita_Pizza()

class Pizza_Store_2(Pizza_Store):
    def create_pizza(self) -> Pizza:
        return Pepperoni_Pizza()
  
# Product interface
class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> None:
        pass

    @abstractmethod
    def bake(self) -> None:
        pass

    @abstractmethod
    def cut(self) -> None:
        pass

    @abstractmethod
    def box(self) -> None:
        pass

# Concrete product implementations
class Margherita_Pizza(Pizza):
    def prepare(self) -> None:
        print("Preparing Margherita Pizza")

    def bake(self) -> None:
        print("Baking Margherita Pizza")

    def cut(self) -> None:
        print("Cutting Margherita Pizza")

    def box(self) -> None:
        print("Boxing Margherita Pizza")

class Pepperoni_Pizza(Pizza):
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
    
