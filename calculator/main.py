# Creating a Module Calculator
class Calculator:

    # result set to 0 for initialization
    result = 0

    # Defining the get_result function
    def get_result(self):
        # to get the latest result
        return self.result

    # Defining the addition function
    def addition(self, value_a, value_b):
        # updates the result of addition of two numbers to global result
        self.result = (value_a + value_b)

        # returns the result
        return self.result

    # Defining the subtraction function
    def subtraction(self, value_a, value_b):
        # updates the result of subtraction of two numbers to global result
        self.result = (value_a - value_b)

        # returns the result
        return self.result

    # Defining the multiplication function
    def multiplication(self, value_a, value_b):
        # updates the result of multiplication of two numbers to global result
        self.result = (value_a * value_b)

        # returns the result
        return self.result

    # Defining the division function
    def division(self, value_a, value_b):
        # updates the result of division of two numbers to global result
        self.result = (value_a / value_b)

        # returns the result
        return self.result
