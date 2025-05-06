class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car brand:", my_car.brand)

# Access public method
my_car.start()


