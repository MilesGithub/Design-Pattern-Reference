

def main():
  
    pizzas = [MargheritaPizza(), PepperoniPizza()]
    description_visitor = PizzaDescriptionVisitor()

    for pizza in pizzas:
        pizza.accept(description_visitor)
        

# Visitor Interface
class PizzaVisitor:
    def visit_margherita(self, margherita):
        pass

    def visit_pepperoni(self, pepperoni):
        pass

# Concrete Visitor
class PizzaDescriptionVisitor(PizzaVisitor):
    def visit_margherita(self, margherita):
        print("Margherita Pizza: Tomato sauce, mozzarella cheese, basil")

    def visit_pepperoni(self, pepperoni):
        print("Pepperoni Pizza: Tomato sauce, mozzarella cheese, pepperoni slices")

# Element Interface
class Pizza:
    def accept(self, visitor):
        pass
      
# Concrete Elements
class MargheritaPizza(Pizza):
    def accept(self, visitor):
        visitor.visit_margherita(self)

class PepperoniPizza(Pizza):
    def accept(self, visitor):
        visitor.visit_pepperoni(self)


if __name__ == "__main__":
    main()
