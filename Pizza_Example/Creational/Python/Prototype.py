import copy

def main():

    margherita_prototype = PizzaPrototype("Margherita", "Thin", "Tomato", ["Mozzarella", "Basil"])
    pepperoni_prototype = PizzaPrototype("Pepperoni", "Thick", "Tomato", ["Pepperoni", "Cheddar Cheese"])
    bbq_prototype = PizzaPrototype("BBQ", "Thick", "BBQ", ["Chicken", "Cheddar Cheese"])

    pizza_menu = PizzaMenu()
    pizza_menu.add_pizza("Margherita", margherita_prototype)
    pizza_menu.add_pizza("Pepperoni", pepperoni_prototype)
    pizza_menu.add_pizza("BBQ", bbq_prototype)

    margherita_pizza = pizza_menu.get_pizza("Margherita")
    pepperoni_pizza = pizza_menu.get_pizza("Pepperoni")
    bbq_pizza = pizza_menu.get_pizza("BBQ")

    custom_margherita = pizza_menu.get_pizza("Margherita", dough="Stuffed", toppings=["Mozzarella","Extra Cheese"])
    custom_pepperoni = pizza_menu.get_pizza("Pepperoni", dough="Stuffed", sauce="BBQ", toppings=["Pepperoni", "Cheddar Cheese", "Onions"])
    custom_bbq = pizza_menu.get_pizza("BBQ", sauce="BBQ", toppings=["Chicken", "Cheddar Cheese", "Hot Peppers"])
    
    print(margherita_pizza)
    print(custom_margherita)
    print("\n")
    print(pepperoni_pizza) 
    print(custom_pepperoni)
    print("\n")
    print(bbq_pizza)
    print(custom_bbq)


class PizzaPrototype:
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def __str__(self):
        return f"{self.name} Pizza with Dough: {self.dough}, Sauce: {self.sauce}, and Toppings: {', '.join(self.toppings)}"

class PizzaMenu:
    def __init__(self):
        self._pizza_prototypes = {}

    def add_pizza(self, name, pizza_prototype):
        self._pizza_prototypes[name] = pizza_prototype

    def remove_pizza(self, name):
        del self._pizza_prototypes[name]

    def get_pizza(self, name, **customizations):
        prototype = copy.deepcopy(self._pizza_prototypes.get(name))
        prototype.__dict__.update(customizations)
        return prototype


if __name__ == "__main__":
    main()
    
