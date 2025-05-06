class Logger:
    # __init__() is the constructor, called when an object is instantiated.
    def __init__(self):
        print("Logger initialized: Object created.")

    # __del__() is the destructor, called when the object is garbage collected or explicitly deleted using del.
    def __del__(self):
        print("Logger finalized: Object destroyed.")

# Example usage
logger1 = Logger()

# You can delete it manually to trigger the destructor immediately
del logger1

# Note: Destructor may also be called automatically when the script ends
