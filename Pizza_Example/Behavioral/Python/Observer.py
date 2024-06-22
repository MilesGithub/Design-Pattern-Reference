def main():
    # Setup the subject and observers
    order_system = OrderSystem()
    customer_app = CustomerApp()
    delivery_person = DeliveryPerson()

    pizza_maker = PizzaMaker()

    # Register observers with the subject
    pizza_maker.add_observer(order_system)
    pizza_maker.add_observer(delivery_person)
    pizza_maker.add_observer(customer_app)
    
    # Trigger an event that notifies all observers
    pizza_maker.make_pizza()

# Observer interface defining the contract for observer classes
class PizzaMakingObserver:
    def update(self, pizza_stage):
        """Receive update from subject."""
        pass

# Concrete Observer - Order System
class OrderSystem(PizzaMakingObserver):
    def update(self, pizza_stage):
        """Action taken by the order system when receiving an update."""
        print(f"Order System: Pizza is now in the {pizza_stage} stage.")

# Concrete Observer - Customer App
class CustomerApp(PizzaMakingObserver):
    def update(self, pizza_stage):
        """Action taken by the customer app when receiving an update."""
        print(f"Customer App: Pizza is now in the {pizza_stage} stage.")

# Concrete Observer - Delivery Person
class DeliveryPerson(PizzaMakingObserver):
    def update(self, pizza_stage):
        """Action taken by the delivery person when receiving an update."""
        print(f"Delivery Person: Pizza is now in the {pizza_stage} stage.")

# Subject that notifies observers about changes
class PizzaMaker:
    def __init__(self):
        self._observers = []  # List of observers

    def add_observer(self, observer):
        """Register an observer."""
        self._observers.append(observer)

    def remove_observer(self, observer):
        """Unregister an observer."""
        self._observers.remove(observer)

    def notify_observers(self, pizza_stage):
        """Notify all registered observers of a change."""
        for observer in self._observers:
            observer.update(pizza_stage)

    def make_pizza(self):
        """Simulate making pizza and notifying observers at each stage."""
        print("Status: Making pizza")
        self.notify_observers("Preparation")

        print("Status: Baking pizza in the oven")
        self.notify_observers("Baking")

        print("Status: Pizza is ready for delivery")
        self.notify_observers("Ready for Delivery")

if __name__ == "__main__":
    main()






