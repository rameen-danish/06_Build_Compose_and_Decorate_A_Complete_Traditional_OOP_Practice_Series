# Engine class with a method to describe its type
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        return f"{self.engine_type} engine started."

# Car class that uses Engine (composition)
class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        # Accessing Engine's method through Car
        return f"{self.make} car: {self.engine.start()}"

# Example usage:
my_engine = Engine("V8")        # Create an Engine object
my_car = Car("Ford Mustang", my_engine)  # Pass Engine object to Car

print(my_car.start_car())  # Access Engine's method through Car
