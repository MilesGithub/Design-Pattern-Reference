def main():
    pizza_system = PizzaOrderSystem()
    pizza_system.place_order("Margherita", "John")
    print("\n")  
    pizza_system.place_order("Pepperoni", "Joe")

# Mediator interface defining the contract for concrete mediators
class PizzaMediator:
    def order_pizza(self, pizza_type: str, customer_name: str):
        """Place an order for a pizza."""
        pass

# Concrete Mediator managing the interaction between the chef and customer service
class PizzaOrderMediator(PizzaMediator):
    def __init__(self):
        # Initializing colleagues within the mediator
        self.chef = PizzaChef(self)
        self.customer_service = CustomerService(self)

    def order_pizza(self, pizza_type: str, customer_name: str):
        """Process pizza orders and delegate tasks to the appropriate colleagues."""
        print(f"Order received for {pizza_type} pizza from {customer_name}.")
        # Ask the chef to prepare the pizza
        self.chef.prepare_pizza(pizza_type)

# Base class for colleagues participating in mediation
class Colleague:
    def __init__(self, mediator: PizzaMediator):
        self.mediator = mediator

# Concrete Colleague responsible for preparing pizzas
class PizzaChef(Colleague):
    def prepare_pizza(self, pizza_type: str):
        """Prepare the pizza and inform customer service when ready."""
        print(f"Chef is preparing {pizza_type} pizza.")
        print(f"{pizza_type} pizza is ready for delivery.")
        # Notify customer service to inform the customer
        self.mediator.customer_service.notify_customer(pizza_type)

# Concrete Colleague responsible for customer communication
class CustomerService(Colleague):
    def notify_customer(self, pizza_type: str):
        """Notify the customer that their pizza is ready."""
        print(f"Customer app is notifying the customer about the {pizza_type} pizza.")

# Client-facing system that customers interact with to place orders
class PizzaOrderSystem:
    def __init__(self):
        # The system uses a mediator to handle ordering process
        self.mediator = PizzaOrderMediator()

    def place_order(self, pizza_type: str, customer_name: str):
        """Place a new pizza order through the mediator."""
        self.mediator.order_pizza(pizza_type, customer_name)

if __name__ == "__main__":
    main()


