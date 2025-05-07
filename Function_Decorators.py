# Define the decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Apply the decorator to the say_hello function
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
