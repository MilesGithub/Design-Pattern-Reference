
def main():

    margherita = Pizza("Margherita")
    margherita.add_topping(PizzaFactory.get_topping("Tomato Sauce"))
    margherita.add_topping(PizzaFactory.get_topping("Cheese"))

    pepperoni = Pizza("Pepperoni")
    pepperoni.add_topping(PizzaFactory.get_topping("Tomato Sauce"))
    pepperoni.add_topping(PizzaFactory.get_topping("Cheese"))
    pepperoni.add_topping(PizzaFactory.get_topping("Pepperoni"))

    veggie = Pizza("Vegetarian")
    veggie.add_topping(PizzaFactory.get_topping("Tomato Sauce"))
    veggie.add_topping(PizzaFactory.get_topping("Cheese"))
    veggie.add_topping(PizzaFactory.get_topping("Mushrooms"))
    veggie.add_topping(PizzaFactory.get_topping("Peppers"))
    veggie.add_topping(PizzaFactory.get_topping("Onions"))

    margherita.bake()
    pepperoni.bake()
    veggie.bake()

class PizzaTopping:
    def __init__(self, name):
        self.name = name

    def add_topping(self, pizza):
        print(f"{self.name}")

class Pizza:
    def __init__(self, name):
        self.name = name
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def bake(self):
        print(f"\nBaking {self.name} pizza with the following toppings:")
        for topping in self.toppings:
            topping.add_topping(self)

class PizzaFactory:
    _topping_cache = {}

    @staticmethod
    def get_topping(name):
        if name not in PizzaFactory._topping_cache:
            PizzaFactory._topping_cache[name] = PizzaTopping(name)
        return PizzaFactory._topping_cache[name]

if __name__ == "__main__":
    main()



