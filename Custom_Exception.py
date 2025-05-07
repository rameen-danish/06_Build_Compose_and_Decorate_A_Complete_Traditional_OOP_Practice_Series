# Define the custom exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check the age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is invalid. Must be 18 or older.")
    else:
        print(f"Age {age} is valid.")

# Example usage
try:
    check_age(15)  # Test with an age below 18
except InvalidAgeError as e:
    print("Caught an exception:", e)

try:
    check_age(20)  # Test with a valid age
except InvalidAgeError as e:
    print("Caught an exception:", e)

