from abc import ABC, abstractmethod

def main():
  
    thin_crust = ThinCrust()
    thick_crust = ThickCrust()

    margherita_thin_crust = MargheritaPizza(thin_crust)
    pepperoni_thick_crust = PepperoniPizza(thick_crust)

    print(margherita_thin_crust.make_pizza())
    print(pepperoni_thick_crust.make_pizza())


# Implementor interface for pizza implementation
class PizzaImplementation(ABC):
    @abstractmethod
    def prepare(self):
        pass

# ConcreteImplementorA: Thin Crust
class ThinCrust(PizzaImplementation):
    def prepare(self):
        return "Thin Crust"

# ConcreteImplementorB: Thick Crust
class ThickCrust(PizzaImplementation):
    def prepare(self):
        return "Thick Crust"

# Abstraction interface for pizza
class Pizza(ABC):
    def __init__(self, implementation):
        self.implementation = implementation

    @abstractmethod
    def make_pizza(self):
        pass

# RefinedAbstractionA: Margherita Pizza
class MargheritaPizza(Pizza):
    def make_pizza(self):
        return f"Margherita Pizza with {self.implementation.prepare()}"

# RefinedAbstractionB: Pepperoni Pizza
class PepperoniPizza(Pizza):
    def make_pizza(self):
        return f"Pepperoni Pizza with {self.implementation.prepare()}"

if __name__ == "__main__":
    main()
