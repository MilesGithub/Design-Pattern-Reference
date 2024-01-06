
def main():
  
    pizza_facade = PizzaOrderFacade()
    pizza_facade.place_order("Margherita", ["Cheese", "Tomato", "Bassil"], 15.99)
    pizza_facade.place_order("Pepperoni", ["Pepperoni", "Cheese", "Tomato"], 18.99)
    pizza_facade.place_order("BBQ", ["Cheese", "Chicken", "Onion"], 19.99)
    
# Subsystem Classes
class PizzaMaker:
    def make_dough(self):
        print("Making pizza dough")

    def add_toppings(self, toppings):
        print(f"Adding toppings: {', '.join(toppings)}")

    def bake_pizza(self):
        print("Baking pizza")


class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment: ${amount}")


class DeliveryService:
    def deliver_order(self):
        print("Delivering the order")


# Facade Class
class PizzaOrderFacade:
    def __init__(self):
        self.pizza_maker = PizzaMaker()
        self.payment_processor = PaymentProcessor()
        self.delivery_service = DeliveryService()

    def place_order(self, pizza_type, toppings, amount):
        print(f"Placing order for {pizza_type} pizza with toppings: {', '.join(toppings)}")

        self.pizza_maker.make_dough()
        self.pizza_maker.add_toppings(toppings)
        self.pizza_maker.bake_pizza()

        self.payment_processor.process_payment(amount)

        self.delivery_service.deliver_order()
        print("Order delivered successfully!\n")


if __name__ == "__main__":
    main()

