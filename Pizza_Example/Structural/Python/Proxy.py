def main():

    real_order = RealPizzaOrder()
    proxy_order = PizzaOrderProxy(real_order)
    proxy_order.make_order()

# Subject interface
class PizzaOrder:
    def make_order(self):
        pass

# RealSubject
class RealPizzaOrder(PizzaOrder):
    def make_order(self):
        print("Pizza order is being prepared.")

# Proxy
class PizzaOrderProxy(PizzaOrder):
    def __init__(self, real_order=None):
        self._real_order = real_order if real_order else RealPizzaOrder()

    def make_order(self):
        print("Proxy: Checking customer")
        self._real_order.make_order()

if __name__ == "__main__":
    main()

