class Student:                                          # __init__ is the constructor method used to initialize the name and marks attributes.
    def __init__(self, name, marks):                    #The self keyword represents the current instance of the class and is used to access variables that belong to the class.
        self.name = name
        self.marks = marks

    def display(self):                                   # display() prints the values stored in the instance.
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Rameen", 90)
student1.display()

student2 = Student("Ayesha", 85)
student2.display()

