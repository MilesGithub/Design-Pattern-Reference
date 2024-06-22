class PizzaIngredients:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def __iter__(self):
        return PizzaIngredientsIterator(self.ingredients)

class PizzaIngredientsIterator:
    def __init__(self, ingredients):
        self._ingredients = ingredients
        self._index = 0

    def __next__(self):
        if self._index < len(self._ingredients):
            ingredient = self._ingredients[self._index]
            self._index += 1
            return ingredient
        else:
            raise StopIteration

    def __iter__(self):
        return self

def main():
    # Create pizza ingredients list
    ingredients = PizzaIngredients()

    # Add ingredients to the list
    ingredients.add_ingredient("Tomato Sauce")
    ingredients.add_ingredient("Mozzarella Cheese")
    ingredients.add_ingredient("Pepperoni")
    ingredients.add_ingredient("Sausage")
    ingredients.add_ingredient("Bacon")
    ingredients.add_ingredient("Mushrooms")
    ingredients.add_ingredient("Onions")
    ingredients.add_ingredient("Bell Peppers")
    ingredients.add_ingredient("Black Olives")
    ingredients.add_ingredient("Basil")
    ingredients.add_ingredient("Garlic")

    print("Display Ingredients\n")

    # Iterate through the ingredients list
    print("Pizza Ingredients:")
    for ingredient in ingredients:
        print(ingredient)

if __name__ == "__main__":
    main()
