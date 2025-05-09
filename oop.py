
class ShoppingCart:
    """
    Definition of the class
    Class is blueprint of creating obj (shopping cart)
    __init__ is the constructor. Runs automatically when you create a new ShoppingCart.
    self.items is an empty list used to store the cart’s items.
    self refers to the instance of the class — the actual cart object.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))  # add_item is a method

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
    """
    loops within the cart to remove the item
    """

    def calculate_total(self) -> float:
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def summary(self):
        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.2f}")  # ✅ Better formatting
        print(f"Total: Ksh {self.calculate_total():.2f}")

# ✅ Moved this outside of the class
if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_item("Kiwi", 69, 30)
    cart.add_item("Mango", 79, 20)
    cart.add_item("Orange", 89, 50)

    cart.summary()

    cart.remove_item("Mango")
    print("\nAfter removing Mango:")
    cart.summary()



