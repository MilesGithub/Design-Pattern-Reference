from copy import deepcopy

def main():
  
    print("New State")
      
    # Initial pizza setup
    pizza = Pizza("Margherita", ["Cheese", "Basil"])
    caretaker = PizzaCaretaker()

    print("Current State:", pizza)
    
    # Saving the initial state of the pizza
    caretaker.add_memento(pizza.create_memento())

    print("Save State\n")
    print("New State")

    # Modifying the pizza's state
    pizza.flavor = "Pepperoni"
    pizza.toppings.append("Pepperoni")

    print("Current State:", pizza)

    # Restoring the pizza's state to the saved state
    pizza.restore_from_memento(caretaker.get_memento(0))
    
    print("\nRestored State")
    print("Current State:", pizza)

# Originator: Manages the state that can be saved and restored
class Pizza:
    def __init__(self, flavor, toppings):
        self.flavor = flavor
        self.toppings = toppings

    def __str__(self):
        return f"{self.flavor} Pizza with {', '.join(self.toppings)} toppings"

    def create_memento(self):
        # Creates a memento object to save the current state
        return PizzaMemento(self.flavor, self.toppings)

    def restore_from_memento(self, memento):
        # Restores the state from the memento
        self.flavor = memento.flavor
        self.toppings = deepcopy(memento.toppings)

# Memento: Stores the internal state of the Originator object.
class PizzaMemento:
    def __init__(self, flavor, toppings):
        self.flavor = flavor
        # Use deepcopy to avoid mutations affecting the memento
        self.toppings = deepcopy(toppings)

# Caretaker: Responsible for keeping the memento
class PizzaCaretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        # Adds a new state snapshot
        self._mementos.append(memento)

    def get_memento(self, index):
        # Retrieves a specific snapshot by index
        return self._mementos[index]

if __name__ == "__main__":
    main()
