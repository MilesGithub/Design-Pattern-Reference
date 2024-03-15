def main():
    # Initialize builders for different pizza types
    margherita_builder = MargheritaPizzaBuilder()
    pepperoni_builder = PepperoniPizzaBuilder()
    bbq_builder = BBQPizzaBuilder()

    # Construct and display Margherita Pizza
    director = PizzaDirector(margherita_builder)
    director.construct_pizza()
    margherita_pizza = director.get_pizza()
    print("Margherita Pizza:")
    print(margherita_pizza)

    # Construct and display Pepperoni Pizza
    director.builder = pepperoni_builder  # Reuse director with a different builder
    director.construct_pizza()
    pepperoni_pizza = director.get_pizza()
    print("Pepperoni Pizza:")
    print(pepperoni_pizza)
    
    # Construct and display BBQ Pizza
    director.builder = bbq_builder  # Reuse director with a different builder
    director.construct_pizza()
    bbq_pizza = director.get_pizza()
    print("BBQ Pizza:")
    print(bbq_pizza)

# Abstract Builder class for pizza construction
class PizzaBuilder:
    def build_dough(self):
        pass

    def build_sauce(self):
        pass

    def build_cheese(self):
        pass

    def build_toppings(self):
        pass

# Director class to manage pizza construction process
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_pizza(self):
        # Directs the construction process
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_cheese()
        self.builder.build_toppings()

    def get_pizza(self):
        # Returns the constructed pizza
        return self.builder.pizza

# Pizza class representing the product to be built
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

    # Format pizza attributes into a string
    def __str__(self):
        return f"Dough: {self.dough}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {', '.join(self.toppings)}"

# Concrete builder for Margherita Pizza
class MargheritaPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()  # Initializes a new pizza instance

    # Implementation of abstract building methods
    def build_dough(self):
        self.pizza.set_dough("Thin Crust")

    def build_sauce(self):
        self.pizza.set_sauce("Tomato Sauce")

    def build_cheese(self):
        self.pizza.set_cheese("Mozzarella Cheese")

    def build_toppings(self):
        self.pizza.set_toppings(["Basil", "Tomatoes"])

# Concrete builder for Pepperoni Pizza
class PepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()  # Initializes a new pizza instance

    # Implementation of abstract building methods
    def build_dough(self):
        self.pizza.set_dough("Thick Crust")

    def build_sauce(self):
        self.pizza.set_sauce("Spicy Tomato Sauce")

    def build_cheese(self):
        self.pizza.set_cheese("Cheddar Cheese")

    def build_toppings(self):
        self.pizza.set_toppings(["Pepperoni", "Green Peppers", "Olives"])

# Concrete builder for BBQ Pizza
class BBQPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()  # Initializes a new pizza instance

    # Implementation of abstract building methods
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
