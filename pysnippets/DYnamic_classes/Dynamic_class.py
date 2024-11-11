# Function to dynamically create a function and assign it to a class
def create_dynamic_function(name, expression):
    def func(self, x, y):
        return eval(expression)
    func.__name__ = name
    return func

# Class to hold dynamic functions
class MathOperations:
    pass

# Adding dynamically created functions to the class
MathOperations.add = create_dynamic_function("add", "x + y")
MathOperations.multiply = create_dynamic_function("multiply", "x * y")

