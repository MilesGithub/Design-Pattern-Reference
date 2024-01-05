
def main():
  
    margherita_builder = MargheritaPizzaBuilder()
    pepperoni_builder = PepperoniPizzaBuilder()
    bbq_builder = BBQPizzaBuilder()

    director = PizzaDirector(margherita_builder)
    director.construct_pizza()
    margherita_pizza = director.get_pizza()

    director = PizzaDirector(pepperoni_builder)
    director.construct_pizza()
    pepperoni_pizza = director.get_pizza()
    
    director = PizzaDirector(bbq_builder)
    director.construct_pizza()
    bbq_pizza = director.get_pizza()

    print("Margherita Pizza:")
    print(margherita_pizza)
    print("Pepperoni Pizza:")
    print(pepperoni_pizza)
    print("BBQ Pizza:")
    print(bbq_pizza)


class PizzaBuilder:
    def build_dough(self):
        pass

    def build_sauce(self):
        pass

    def build_cheese(self):
        pass

    def build_toppings(self):
        pass

# Director
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_cheese()
        self.builder.build_toppings()

    def get_pizza(self):
        return self.builder.pizza

# Product
class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.cheese = ""
        self.toppings = []

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_cheese(self, cheese):
        self.cheese = cheese

    def set_toppings(self, toppings):
        self.toppings = toppings

    def __str__(self):
        return f"Dough: {self.dough}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {', '.join(self.toppings)}"

# Concrete builder Margherita
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("Thin Crust")

    def build_sauce(self):
        self.pizza.set_sauce("Tomato Sauce")

    def build_cheese(self):
        self.pizza.set_cheese("Mozzarella Cheese")

    def build_toppings(self):
        self.pizza.set_toppings(["Basil", "Tomatoes"])

# Concrete builder Pepperoni
class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("Thick Crust")

    def build_sauce(self):
        self.pizza.set_sauce("Spicy Tomato Sauce")

    def build_cheese(self):
        self.pizza.set_cheese("Cheddar Cheese")

    def build_toppings(self):
        self.pizza.set_toppings(["Pepperoni", "Green Peppers", "Olives"])

# Concrete builder BBQ
class BBQPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("Thick Crust")

    def build_sauce(self):
        self.pizza.set_sauce("BBQ Sauce")

    def build_cheese(self):
        self.pizza.set_cheese("Cheddar Cheese")

    def build_toppings(self):
        self.pizza.set_toppings(["Chicken", "Onions"])


if __name__ == "__main__":
    main()
    
