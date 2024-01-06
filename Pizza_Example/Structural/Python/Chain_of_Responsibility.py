
def main():
  
    pizza_maker = PizzaMaker()
    
    order_with_cheese = PizzaOrder(["dough", "sauce", "cheese"])
    pizza_maker.prepare_pizza(order_with_cheese)
    
    order_without_sauce = PizzaOrder(["dough", "cheese"])
    pizza_maker.prepare_pizza(order_without_sauce)
    
    order_with_extra_toppings = PizzaOrder(["dough", "sauce", "cheese", "pepperoni"])
    pizza_maker.prepare_pizza(order_with_extra_toppings)


# Handler interface
class PizzaHandler:
    def set_successor(self, successor):
        pass

    def handle_order(self, order):
        pass

# Concrete handler 1: Dough Preparation
class DoughHandler(PizzaHandler):
    def set_successor(self, successor):
        self.successor = successor
    
    def handle_order(self, order):
        if "dough" in order:
            print("DoughHandler: Preparing dough for the pizza")
        elif self.successor is not None:
            self.successor.handle_order(order)

# Concrete handler 2: Sauce Application
class SauceHandler(PizzaHandler):
    def set_successor(self, successor):
        self.successor = successor
    
    def handle_order(self, order):
        if "sauce" in order:
            print("SauceHandler: Applying sauce to the pizza")
        elif self.successor is not None:
            self.successor.handle_order(order)

# Concrete handler 3: Cheese Application
class CheeseHandler(PizzaHandler):
    def set_successor(self, successor):
        self.successor = successor
    
    def handle_order(self, order):
        if "cheese" in order:
            print("CheeseHandler: Sprinkling cheese on the pizza")
        elif self.successor is not None:
            self.successor.handle_order(order)

# Client: Pizza Order
class PizzaOrder:
    def __init__(self, order):
        self.order = order

# Client: PizzaMaker
class PizzaMaker:
    def __init__(self):
        # Create the chain of pizza preparation handlers
        dough_handler = DoughHandler()
        sauce_handler = SauceHandler()
        cheese_handler = CheeseHandler()
        
        dough_handler.set_successor(sauce_handler)
        sauce_handler.set_successor(cheese_handler)
        
        self.handler = dough_handler
    
    def prepare_pizza(self, pizza_order):
        print("Preparing pizza:")
        self.handler.handle_order(pizza_order.order)
        print("Pizza is ready!")


if __name__ == "__main__":
    main()
