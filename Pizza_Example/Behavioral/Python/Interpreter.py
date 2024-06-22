from abc import ABC, abstractmethod

# Context that holds the state of the pizza store
class PizzaStoreContext:
    def __init__(self):
        self.orders = {}

    def add_order(self, order_id, pizza_type):
        self.orders[order_id] = {'type': pizza_type, 'Status': 'Ordered'}
        print(f"Order {order_id}: {pizza_type} pizza ordered.")

    def check_status(self, order_id):
        if order_id in self.orders:
            print(f"Order {order_id} Status: {self.orders[order_id]['Status']}.")
        else:
            print(f"Order {order_id} Not found.")

    def cancel_order(self, order_id):
        if order_id in self.orders:
            del self.orders[order_id]
            print(f"Order {order_id} Cancelled.")
        else:
            print(f"Order {order_id} Not found.")

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

# Terminal Expression for ordering pizza
class OrderPizzaExpression(Expression):
    def __init__(self, order_id, pizza_type):
        self.order_id = order_id
        self.pizza_type = pizza_type

    def interpret(self, context):
        context.add_order(self.order_id, self.pizza_type)

# Terminal Expression for checking order status
class CheckStatusExpression(Expression):
    def __init__(self, order_id):
        self.order_id = order_id

    def interpret(self, context):
        context.check_status(self.order_id)

# Terminal Expression for cancelling an order
class CancelOrderExpression(Expression):
    def __init__(self, order_id):
        self.order_id = order_id

    def interpret(self, context):
        context.cancel_order(self.order_id)

# Client
def main():
    # Create the context
    context = PizzaStoreContext()

    # Create some expressions
    expressions = [
        OrderPizzaExpression(1, "Margherita"),
        OrderPizzaExpression(2, "Pepperoni"),
        CheckStatusExpression(1),
        CancelOrderExpression(1),
        CheckStatusExpression(1),
        CheckStatusExpression(2)
    ]

    # Interpret the expressions
    for expr in expressions:
        expr.interpret(context)

if __name__ == "__main__":
    main()




