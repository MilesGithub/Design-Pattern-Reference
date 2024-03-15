import copy

def main():
    # Initialize pizza prototypes with their default attributes
    margherita_prototype = PizzaPrototype("Margherita", "Thin", "Tomato", ["Mozzarella", "Basil"])
    pepperoni_prototype = PizzaPrototype("Pepperoni", "Thick", "Tomato", ["Pepperoni", "Cheddar Cheese"])
    bbq_prototype = PizzaPrototype("BBQ", "Thick", "BBQ", ["Chicken", "Cheddar Cheese"])

    # Create a pizza menu and add the prototypes
    pizza_menu = PizzaMenu()
    pizza_menu.add_pizza("Margherita", margherita_prototype)
    pizza_menu.add_pizza("Pepperoni", pepperoni_prototype)
    pizza_menu.add_pizza("BBQ", bbq_prototype)

    # Retrieve standard pizza prototypes
    margherita_pizza = pizza_menu.get_pizza("Margherita")
    pepperoni_pizza = pizza_menu.get_pizza("Pepperoni")
    bbq_pizza = pizza_menu.get_pizza("BBQ")

    # Customize pizza prototypes with additional or modified attributes
    custom_margherita = pizza_menu.get_pizza("Margherita", dough="Stuffed", toppings=["Mozzarella", "Extra Cheese"])
    custom_pepperoni = pizza_menu.get_pizza("Pepperoni", dough="Stuffed", sauce="BBQ", toppings=["Pepperoni", "Cheddar Cheese", "Onions"])
    custom_bbq = pizza_menu.get_pizza("BBQ", sauce="BBQ", toppings=["Chicken", "Cheddar Cheese", "Hot Peppers"])

    # Print the details of the original and customized pizzas
    print(margherita_pizza)
    print(custom_margherita)
    print("\n")
    print(pepperoni_pizza)
    print(custom_pepperoni)
    print("\n")
    print(bbq_pizza)
    print(custom_bbq)

class PizzaPrototype:
    # Initialize a new pizza prototype with its properties
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    # String representation for easy printing
    def __str__(self):
        return f"{self.name} Pizza with Dough: {self.dough}, Sauce: {self.sauce}, and Toppings: {', '.join(self.toppings)}"

class PizzaMenu:
    # Initialize an empty dictionary to store pizza prototypes
    def __init__(self):
        self._pizza_prototypes = {}

    # Add a new pizza prototype to the menu
    def add_pizza(self, name, pizza_prototype):
        self._pizza_prototypes[name] = pizza_prototype

    # Remove a pizza prototype from the menu by name
    def remove_pizza(self, name):
        del self._pizza_prototypes[name]

    # Clone a pizza prototype and optionally customize it
    def get_pizza(self, name, **customizations):
        # Deep copy ensures a new object instance, preventing modifications to the original prototype
        prototype = copy.deepcopy(self._pizza_prototypes.get(name))
        # Apply customizations to the copied prototype
        prototype.__dict__.update(customizations)
        return prototype

if __name__ == "__main__":
    main()
