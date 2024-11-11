# Dynamic attribute assignment to a class instance
class Config:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

# Creating a config object dynamically with different attributes
config = Config(database="MySQL", user="admin", password="securepass")
