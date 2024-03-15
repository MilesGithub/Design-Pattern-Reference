from abc import ABC, abstractmethod

def main():
    # Initialize individual basic pizzas
    margherita = BasicPizza()
    pepperoni = BasicPizza()
    bbq = BasicPizza()
    
    print("#----Adding Toppings----#")
    # Add toppings to individual pizzas
    margherita.add_topping("Tomato Sauce")
    margherita.add_topping("Mozzarella")
    
    pepperoni.add_topping("Tomato Sauce")
    pepperoni.add_topping("Mozzarella")
    pepperoni.add_topping("Pepperoni")

    bbq.add_topping("BBQ Sauce")
    bbq.add_topping("Cheddar Cheese")
    bbq.add_topping("Chicken")
    
    # Create a combo pizza and add individual pizzas to it
    combo_pizza = ComboPizza()
    combo_pizza.add_pizza(margherita)
    combo_pizza.add_pizza(pepperoni)
    combo_pizza.add_pizza(bbq)
    
    # Add a topping to the combo pizza, which in turn adds the topping to all its pizzas
    combo_pizza.add_topping("Onions")

    print("\n#----Baking----#")
    # Bake individual and combo pizzas
    margherita.bake()
    pepperoni.bake()
    bbq.bake()
    combo_pizza.bake()

# Abstract Component
class PizzaComponent(ABC):
    @abstractmethod
    def add_topping(self, topping):
        #Add a topping to the pizza.
        pass

    @abstractmethod
    def bake(self):
        #Bake the pizza.
        pass

# Leaf Component
class BasicPizza(PizzaComponent):
    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"Adding {topping} to the pizza")

    def bake(self):
        print("Baking the pizza with toppings:", ', '.join(self.toppings))

# Composite Component
class ComboPizza(PizzaComponent):
    def __init__(self):
        self.pizzas = []

    def add_topping(self, topping):
        for pizza in self.pizzas:
            pizza.add_topping(topping)
        print(f"Adding {topping} to the combo pizza")

    def bake(self):
        print("\nBaking the combo pizza with combined toppings.")
        for pizza in self.pizzas:
            pizza.bake()

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        print("Adding a pizza to the combo")

if __name__ == "__main__":
    main()
