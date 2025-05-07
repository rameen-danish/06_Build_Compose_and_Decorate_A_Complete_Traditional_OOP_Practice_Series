class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    # __call__ makes the object callable like a function
    def __call__(self, value):
        return value * self.factor

# Example usage
m = Multiplier(5)  # Create a Multiplier object with a factor of 5

# Test if the object is callable
print(callable(m))  # True, because __call__ is implemented

# Call the object like a function
result = m(10)  # This invokes the __call__ method
print(result)  # Output: 50 (10 * 5)
