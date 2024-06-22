from abc import ABC, abstractmethod

def main():
  
    margherita_order = MargheritaPizzaOrder()
    print("Ordering Margherita Pizza:")
    margherita_order.order_pizza()

    print("\n")

    pepperoni_order = PepperoniPizzaOrder()
    print("Ordering Pepperoni Pizza:")
    pepperoni_order.order_pizza()

# Abstract class defining the template method
class PizzaOrderTemplate(ABC):
    def order_pizza(self):
        self.choose_crust()
        self.add_toppings()
        self.bake()
        self.cut()
        self.box()

    # Concrete method with a default implementation
    def bake(self):
        print("Baking the pizza in the oven")

    # Concrete method with a default implementation
    def cut(self):
        print("Cutting the pizza into slices")

    # Concrete method with a default implementation
    def box(self):
        print("Placing the pizza in a box")

    # Abstract methods that must be implemented by subclasses
    @abstractmethod
    def choose_crust(self):
        pass

    @abstractmethod
    def add_toppings(self):
        pass

# Concrete subclass for ordering a Margherita pizza
class MargheritaPizzaOrder(PizzaOrderTemplate):
    def choose_crust(self):
        print("Choosing thin crust for Margherita pizza")

    def add_toppings(self):
        print("Adding tomato sauce, mozzarella cheese, and fresh basil for Margherita pizza")

# Concrete subclass for ordering a Pepperoni pizza
class PepperoniPizzaOrder(PizzaOrderTemplate):
    def choose_crust(self):
        print("Choosing traditional crust for Pepperoni pizza")

    def add_toppings(self):
        print("Adding tomato sauce, mozzarella cheese, and pepperoni slices for Pepperoni pizza")

if __name__ == "__main__":
    main()
