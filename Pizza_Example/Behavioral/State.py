def main():
    # Initialize the context
    pizza_order = PizzaOrder()

    # Trigger state transitions
    pizza_order.process_order()  # From OrderPlaced to PaymentPending
    pizza_order.process_order()  # From PaymentPending to OrderConfirmed
    pizza_order.process_order()  # From OrderConfirmed to PizzaReady
    pizza_order.process_order()  # From PizzaReady to Delivered
    pizza_order.process_order()  # Attempt to process beyond Delivered (no effect)

class PizzaOrder:
    def __init__(self):
        # Initial state
        self._state = OrderPlacedState()

    def set_state(self, state):
        # Update the current state
        self._state = state

    def process_order(self):
        # Delegate the behavior to the current state
        self._state.handle(self)

# State interface
class PizzaOrderState:
    def handle(self, context):
        """Handle the order process based on the current state."""
        pass

# Concrete state: Order Placed
class OrderPlacedState(PizzaOrderState):
    def handle(self, context):
        print("Pizza order placed. Waiting for payment.")
        # Transition to the next state
        context.set_state(PaymentPendingState())

# Concrete state: Payment Pending
class PaymentPendingState(PizzaOrderState):
    def handle(self, context):
        print("Payment pending. Waiting for payment confirmation.")
        # Transition to the next state
        context.set_state(OrderConfirmedState())

# Concrete state: Order Confirmed
class OrderConfirmedState(PizzaOrderState):
    def handle(self, context):
        print("Order confirmed. Preparing the pizza.")
        # Transition to the next state
        context.set_state(PizzaReadyState())

# Concrete state: Pizza Ready
class PizzaReadyState(PizzaOrderState):
    def handle(self, context):
        print("Pizza is ready for delivery.")
        # Transition to the next state
        context.set_state(DeliveredState())

# Concrete state: Delivered
class DeliveredState(PizzaOrderState):
    def handle(self, context):
        print("Pizza delivered. Enjoy your meal!")
        # In this final state, there are no further transitions

if __name__ == "__main__":
    main()
