
def main():
  
    pizza_shop_1 = PizzaShop()
    pizza_shop_2 = PizzaShop()
    
    pizza_shop_1.order_pizza("Margherita")
    pizza_shop_2.order_pizza("Pepperoni")
    pizza_shop_2.order_pizza("BBQ")
    
    print("\n")
    # Both instances refer to the same pizza shop
    print(pizza_shop_1 is pizza_shop_2)  # True
    print(pizza_shop_1.get_total_pizzas_sold())
    print(pizza_shop_2.get_total_pizzas_sold())
  

class PizzaShop:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PizzaShop, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.pizzas_sold = 0

    def order_pizza(self, flavor):
        self.pizzas_sold += 1
        print(f"Order received! {flavor} pizza is being prepared.")

    def get_total_pizzas_sold(self):
        return self.pizzas_sold


if __name__ == "__main__":
    main()
    
