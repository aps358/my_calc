""" Calculation Abstract Class """

class Calculation:

    # Constructor and first method when object is Instantiated
    def __init__(self, value_a, value_b):
        # self references the instantiated object of the class
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a, value_b)

