def main():
    pizza_maker = PizzaMaker()
    pizza_store_adapter = PizzaAdapter(pizza_maker)
    order_result = pizza_store_adapter.order_pizza()
    print(order_result)

# Target interface
class PizzaStore:
    def order_pizza(self):
        pass

# Adaptee
class PizzaMaker:
    def make_pizza(self):
        return "Pepperoni Pizza"

# Adapter
class PizzaAdapter(PizzaStore):
    def __init__(self, pizza_maker):
        self.pizza_maker = pizza_maker

    def order_pizza(self):
        # Call the make_pizza method of PizzaMaker from the order_pizza method of PizzaStore
        return f"Adapter: {self.pizza_maker.make_pizza()}"

if __name__ == "__main__":
    main()
