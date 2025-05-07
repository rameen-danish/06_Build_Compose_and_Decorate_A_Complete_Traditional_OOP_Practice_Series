# Define the class decorator
def add_greeting(cls):
    # Define a new method to add
    def greet(self):
        return "Hello from Decorator!"
    
    # Attach the method to the class
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Alice")
print(p.greet())  # This method was added by the decorator
