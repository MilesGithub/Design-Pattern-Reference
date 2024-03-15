def main():
    # Initialize two references to what may seem like separate pizza shops
    pizza_shop_1 = PizzaShop()
    pizza_shop_2 = PizzaShop()
    
    # Order pizzas from what seems to be two shops
    pizza_shop_1.order_pizza("Margherita")
    pizza_shop_2.order_pizza("Pepperoni")
    pizza_shop_2.order_pizza("BBQ")
    
    print("\nChecking if both shops are the same instance:")
    # Verify that both variables indeed reference the same object
    print(pizza_shop_1 is pizza_shop_2)  # Expected to be True
    # Display the total pizzas sold by the seemingly two shops
    print(pizza_shop_1.get_total_pizzas_sold())  # Total orders from the single instance
    print(pizza_shop_2.get_total_pizzas_sold())  # Same as above, demonstrating shared state

class PizzaShop:
    _instance = None  # Class attribute to store the singleton instance
    _initialized = False  # Prevents re-initialization of the instance attributes

    def __new__(cls):
        # Ensure only one instance is created
        if cls._instance is None:
            cls._instance = super(PizzaShop, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize instance attributes only once
        if not self._initialized:
            self._initialized = True
            self.pizzas_sold = 0  # Initialize the counter for pizzas sold

    def order_pizza(self, flavor):
        # Process a pizza order
        self.pizzas_sold += 1
        print(f"Order received! {flavor} pizza is being prepared.")

    def get_total_pizzas_sold(self):
        # Return the total number of pizzas sold
        return self.pizzas_sold

if __name__ == "__main__":
    main()
