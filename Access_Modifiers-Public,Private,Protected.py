class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

# Create an object
emp = Employee("Alice", 50000, "123-45-6789")

# Access public variable - This will work
print("Public (name):", emp.name)

# Access protected variable - This will work, but by convention should be treated as protected
print("Protected (_salary):", emp._salary)

# Access private variable - This will raise an AttributeError
try:
    print("Private (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable __ssn:", e)

# Access private variable using name mangling (not recommended, but possible)
print("Accessing private __ssn with name mangling:", emp._Employee__ssn)
