class Counter:
    # Class variable to keep track of the number of objects
    count = 0

    def __init__(self):
        # Increment the class variable each time a new object is created
        Counter.count += 1

    # Class method to access the class variable using cls
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj1 = Counter()

# Display the count of objects
Counter.display_count()
