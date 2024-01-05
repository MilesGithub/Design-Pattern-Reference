from abc import ABC, abstractmethod

def main():

    margherita = BasicPizza()
    pepperoni = BasicPizza()
    bbq = BasicPizza()
    
    print("#----Adding Toppings----#")
    margherita.add_topping("Tomato Sauce")
    margherita.add_topping("Mozzarella")
    
    pepperoni.add_topping("Tomato Sauce")
    pepperoni.add_topping("Mozzarella")
    pepperoni.add_topping("Pepperoni")

    bbq.add_topping("BBQ Sauce")
    bbq.add_topping("Cheddar Cheese")
    bbq.add_topping("Chicken")
    
    combo_pizza = ComboPizza()
    combo_pizza.add_pizza(margherita)
    combo_pizza.add_pizza(pepperoni)
    combo_pizza.add_pizza(bbq)
    
    combo_pizza.add_topping("Onions")

    print("\n#----Baking----#")
    margherita.bake()
    pepperoni.bake()
    bbq.bake()
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
        print("\nBaking the combo pizza:")
        for pizza in self.pizzas:
            pizza.bake()

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)


if __name__ == "__main__":
    main()
    
