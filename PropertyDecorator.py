class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            print("Setting price...")
            self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage:
p = Product(100)
print(p.price)       # Calls the getter
p.price = 150        # Calls the setter
print(p.price)
del p.price          # Calls the deleter
