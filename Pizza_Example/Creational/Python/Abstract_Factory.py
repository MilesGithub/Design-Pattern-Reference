from abc import ABC, abstractmethod

# Main function to demonstrate the creation of different pizza types using the Abstract Factory Pattern
def main():
    # Instantiate factories for each pizza type
    margherita_factory = MargheritaPizzaFactory()
    pepperoni_factory = PepperoniPizzaFactory()
    bbq_factory = BBQPizzaFactory()

    # Create pizzas using the factories
    margherita_dough, margherita_sauce, margherita_cheese = create_pizza(margherita_factory)
    pepperoni_dough, pepperoni_sauce, pepperoni_cheese = create_pizza(pepperoni_factory)
    bbq_dough, bbq_sauce, bbq_cheese = create_pizza(bbq_factory)

    # Display the ingredients of each pizza
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

# Function to create a pizza using a given factory
def create_pizza(factory):
    dough = factory.create_dough()
    sauce = factory.create_sauce()
    cheese = factory.create_cheese()
    return dough, sauce, cheese

# Abstract Factory Interface for creating pizza ingredients
class PizzaFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

# Concrete Factory for creating Margherita Pizza ingredients
class MargheritaPizzaFactory(PizzaFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return TomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

# Concrete Factory for creating Pepperoni Pizza ingredients
class PepperoniPizzaFactory(PizzaFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return SpicyTomatoSauce()

    def create_cheese(self):
        return CheddarCheese()

# Concrete Factory for creating BBQ Pizza ingredients
class BBQPizzaFactory(PizzaFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return BBQSauce()

    def create_cheese(self):
        return CheddarCheese()

# Abstract Product Class for Dough
class Dough(ABC):
    @abstractmethod
    def description(self):
        pass

class ThinCrustDough(Dough):
    def description(self):
        return "Thin crust dough"

class ThickCrustDough(Dough):
    def description(self):
        return "Thick crust dough"

# Abstract Product Class for Sauce
class Sauce(ABC):
    @abstractmethod
    def description(self):
        pass

class TomatoSauce(Sauce):
    def description(self):
        return "Tomato sauce"

class SpicyTomatoSauce(Sauce):
    def description(self):
        return "Spicy tomato sauce"

class BBQSauce(Sauce):
    def description(self):
        return "BBQ sauce"

# Abstract Product Class for Cheese
class Cheese(ABC):
    @abstractmethod
    def description(self):
        pass

class MozzarellaCheese(Cheese):
    def description(self):
        return "Mozzarella cheese"

class CheddarCheese(Cheese):
    def description(self):
        return "Cheddar cheese"

if __name__ == "__main__":
    main()
