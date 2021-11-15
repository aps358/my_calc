""" Calculation Abstract Class """


class Calculation:
    """ Defining Class Constructor in here """
    def __init__(self, value_a, value_b):
        # self references the instantiated object of the class
        self.value_a = value_a
        self.value_b = value_b

    @property
    def value_a(self):
        """ Some value_a """
        return self.value_a

    @property
    def value_b(self):
        """ Some value_b """
        return self.value_b

    # Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        """ Returning the values back """
        return cls(value_a, value_b)
