from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to be implemented by subclasses

# Derived class that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Implementing the abstract method
        return self.width * self.height

# Example usage
rectangle = Rectangle(10, 5)
print("Area of Rectangle:", rectangle.area())
