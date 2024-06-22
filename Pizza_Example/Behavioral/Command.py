from abc import ABC, abstractmethod

# Receiver
class PizzaStore:
    def __init__(self):
        self.orders = {}

    def add_order(self, order_id, pizza_type):
        self.orders[order_id] = {'type': pizza_type, 'status': 'Ordered'}
        print(f"Order {order_id}: {pizza_type} pizza ordered.")

    def check_status(self, order_id):
        if order_id in self.orders:
            print(f"Order {order_id} status: {self.orders[order_id]['status']}.")
        else:
            print(f"Order {order_id} not found.")

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f"Order {order_id} cancelled.")
        else:
            print(f"Order {order_id} not found.")

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command for placing an order
class PlaceOrderCommand(Command):
    def __init__(self, store, order_id, pizza_type):
        self.store = store
        self.order_id = order_id
        self.pizza_type = pizza_type

    def execute(self):
        self.store.add_order(self.order_id, self.pizza_type)

# Concrete Command for checking order status
class CheckStatusCommand(Command):
    def __init__(self, store, order_id):
        self.store = store
        self.order_id = order_id

    def execute(self):
        self.store.check_status(self.order_id)

# Concrete Command for cancelling an order
class CancelOrderCommand(Command):
    def __init__(self, store, order_id):
        self.store = store
        self.order_id = order_id

    def execute(self):
        self.store.cancel_order(self.order_id)

# Invoker
class CommandInvoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()
        self.commands = []  # Clear commands after execution

# Client
def main():
    # Create the receiver
    store = PizzaStore()

    # Create commands
    place_order1 = PlaceOrderCommand(store, 1, "Margherita")
    place_order2 = PlaceOrderCommand(store, 2, "Pepperoni")
    check_status1 = CheckStatusCommand(store, 1)
    cancel_order1 = CancelOrderCommand(store, 1)
    check_status2 = CheckStatusCommand(store, 1)
    check_status3 = CheckStatusCommand(store, 2)

    # Create the invoker
    invoker = CommandInvoker()

    # Add commands to the invoker
    invoker.add_command(place_order1)
    invoker.add_command(place_order2)
    invoker.add_command(check_status1)
    invoker.add_command(cancel_order1)
    invoker.add_command(check_status2)
    invoker.add_command(check_status3)

    # Execute commands
    invoker.execute_commands()

if __name__ == "__main__":
    main()
    
    
    
    
    
    
