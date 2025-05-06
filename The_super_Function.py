# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        # Call the base class constructor using super()
        super().__init__(name)
        self.subject = subject
        print(f"Teacher constructor called for Subject: {self.subject}")

    def display_info(self):
        print(f"Name: {self.name},\nSubject: {self.subject}")

# Example usage
teacher1 = Teacher("Sir Anas", "Python")
teacher1.display_info()
