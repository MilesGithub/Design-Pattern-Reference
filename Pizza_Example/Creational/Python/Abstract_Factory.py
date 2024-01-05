
def main():
  
    margherita_factory = MargheritaPizzaFactory()
    pepperoni_factory = PepperoniPizzaFactory()
    bbq_factory = BBQPizzaFactory()

    margherita_dough, margherita_sauce, margherita_cheese = create_pizza(margherita_factory)
    pepperoni_dough, pepperoni_sauce, pepperoni_cheese = create_pizza(pepperoni_factory)
    bbq_dough, bbq_sauce, bbq_cheese = create_pizza(bbq_factory)

    print("Margherita Pizza Ingredients:")
    print(margherita_dough.description())
    print(margherita_sauce.description())
    print(margherita_cheese.description())

    print("\nPepperoni Pizza Ingredients:")
    print(pepperoni_dough.description())
    print(pepperoni_sauce.description())
    print(pepperoni_cheese.description())
    
    print("\nBBQ Chicken Pizza Ingredients:")
    print(bbq_dough.description())
    print(bbq_sauce.description())
    print(bbq_cheese.description())
    

def create_pizza(factory):
    dough = factory.create_dough()
    sauce = factory.create_sauce()
    cheese = factory.create_cheese()
    return dough, sauce, cheese
  
    
#------Pizza------#
# Abstract Factory Interface
class PizzaFactory:
    def create_dough(self):
        pass

    def create_sauce(self):
        pass

    def create_cheese(self):
        pass

# Concrete Factory for Margherita Pizza
class MargheritaPizzaFactory(PizzaFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return TomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

# Concrete Factory for Pepperoni Pizza
class PepperoniPizzaFactory(PizzaFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return SpicyTomatoSauce()

    def create_cheese(self):
        return CheddarCheese()

# Concrete Factory for BBQ Pizza
class BBQPizzaFactory(PizzaFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return BBQSauce()

    def create_cheese(self):
        return CheddarCheese()


#------Dough------#
# Abstract Product: Dough
class Dough:
    def description(self):
        pass

# Concrete Products for Dough
class ThinCrustDough(Dough):
    def description(self):
        return "Thin crust dough"

class ThickCrustDough(Dough):
    def description(self):
        return "Thick crust dough"


#------Sauce------#
# Abstract Product: Sauce
class Sauce:
    def description(self):
        pass

# Concrete Products for Sauce
class TomatoSauce(Sauce):
    def description(self):
        return "Tomato sauce"

class SpicyTomatoSauce(Sauce):
    def description(self):
        return "Spicy tomato sauce"

class BBQSauce(Sauce):
    def description(self):
        return "BBQ sauce"
      
      
#------Cheese------#
# Abstract Product: Cheese
class Cheese:
    def description(self):
        pass

# Concrete Products for Cheese
class MozzarellaCheese(Cheese):
    def description(self):
        return "Mozzarella cheese"

class CheddarCheese(Cheese):
    def description(self):
        return "Cheddar cheese"



if __name__ == "__main__":
    main()
    

