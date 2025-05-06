class MathUtils:
    # Static method that does not use class (cls) or instance (self)
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
result = MathUtils.add(15,15)
print("Sum:", result)
