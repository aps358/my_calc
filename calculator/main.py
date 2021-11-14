class Calculator:

    # result set to 0 for initialization
    result = 0

    def get_result(self):
        # to get the latest result
        return self.result

    def addition(self, value_a, value_b):
        # to add the result of addition of two numbers to global result
        self.result = (value_a + value_b)

        # updates the latest result to the result
        return self.result

    def subtraction(self, value_a, value_b):
        # to add the result of subtraction of two numbers to global result
        self.result = (value_a - value_b)

        # updates the latest result to the result
        return self.result

    def multiplication(self, value_a, value_b):
        # to add the result of multiplication of two numbers to global result
        self.result = (value_a * value_b)

        # updates the latest result to the result
        return self.result

    def division(self, value_a, value_b):
        # to add the result of division of two numbers to global result
        self.result = (value_a / value_b)

        # updates the latest result to the result
        return self.result