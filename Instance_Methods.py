class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Bella", "Beagle")

# Calling the instance method bark
dog1.bark()
dog2.bark()
