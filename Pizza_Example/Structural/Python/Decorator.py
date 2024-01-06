
def main():

    margherita = Margherita()
    print(f"Cost of {margherita.get_description()}: ${margherita.cost()}")
    
    cheese_pizza = Cheese(margherita)
    print(f"Cost of {cheese_pizza.get_description()}: ${cheese_pizza.cost()}")
    
    pepperoni_veggie_pizza = Veggie(Pepperoni(margherita))
    print(f"Cost of {pepperoni_veggie_pizza.get_description()}: ${pepperoni_veggie_pizza.cost()}")


# Component interface
class Pizza:
    def get_description(self):
        pass

    def cost(self):
        pass

# Concrete component
class Margherita(Pizza):
    def get_description(self):
        return "Margherita Pizza"

    def cost(self):
        return 8

# Decorator
class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_description(self):
        return self._pizza.get_description()

    def cost(self):
        return self._pizza.cost()

# Concrete decorators
class Cheese(PizzaDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Cheese"

    def cost(self):
        return self._pizza.cost() + 2

class Pepperoni(PizzaDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Pepperoni"

    def cost(self):
        return self._pizza.cost() + 3

class Veggie(PizzaDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Veggie"

    def cost(self):
        return self._pizza.cost() + 4


if __name__ == "__main__":
    main()
