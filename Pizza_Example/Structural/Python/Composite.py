from abc import ABC, abstractmethod

def main():
  
    margherita = BasicPizza()
    pepperoni = BasicPizza()

    # Adding toppings to basic pizzas
    margherita.add_topping("Tomato Sauce")
    margherita.add_topping("Mozzarella")
    pepperoni.add_topping("Tomato Sauce")
    pepperoni.add_topping("Mozzarella")
    pepperoni.add_topping("Pepperoni")

    # Creating a combo pizza and adding basic pizzas
    combo_pizza = ComboPizza()
    combo_pizza.add_pizza(margherita)
    combo_pizza.add_pizza(pepperoni)

    # Adding a common topping to the combo pizza
    combo_pizza.add_topping("Olives")

    # Baking the pizzas
    print("\nBaking the Margherita pizza:")
    margherita.bake()

    print("\nBaking the Pepperoni pizza:")
    pepperoni.bake()

    print("\nBaking the Combo pizza:")
    combo_pizza.bake()

# Component
class PizzaComponent(ABC):
    @abstractmethod
    def add_topping(self, topping):
        pass

    @abstractmethod
    def bake(self):
        pass

# Leaf
class BasicPizza(PizzaComponent):
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"Adding {topping} to the pizza")

    def bake(self):
        print("Baking the pizza with toppings:", ', '.join(self.toppings))

# Composite
class ComboPizza(PizzaComponent):
    def __init__(self):
        self.pizzas = []

    def add_topping(self, topping):
        for pizza in self.pizzas:
            pizza.add_topping(topping)

    def bake(self):
        print("Baking the combo pizza:")
        for pizza in self.pizzas:
            pizza.bake()

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)


if __name__ == "__main__":
    main()

