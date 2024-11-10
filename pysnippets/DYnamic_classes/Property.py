# Function to create dynamic properties in a class
def create_dynamic_property(name, initial_value=None):
    def getter(self):
        return getattr(self, f"_{name}", initial_value)
    
    def setter(self, value):
        setattr(self, f"_{name}", value)
    
    return property(getter, setter)

# Class to use dynamic properties
class UserProfile:
    name = create_dynamic_property("name")
    age = create_dynamic_property("age")

# Creating an instance and setting dynamic properties
user = UserProfile()
user.name = "Alice"
user.age = 25
