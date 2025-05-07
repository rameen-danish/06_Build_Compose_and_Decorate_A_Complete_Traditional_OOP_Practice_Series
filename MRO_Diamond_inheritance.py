# Base class A
class A:
    def show(self):
        print("A's show() method")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("B's show() method")

# Class C also inherits from A and overrides show()
class C(A):
    def show(self):
        print("C's show() method")

# Class D inherits from both B and C (diamond inheritance)
class D(B, C):
    pass  # No override here, so MRO decides which show() to use

# Create an instance of D and call show()
d = D()
d.show()

# Print the MRO to understand the method resolution order
print("MRO:", [cls.__name__ for cls in D.__mro__])
