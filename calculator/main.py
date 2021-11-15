""" import all the methods from calc_methods"""
from calc_methods.addition import Addition
from calc_methods.subtraction import Subtraction
from calc_methods.multiplication import Multiplication
from calc_methods.division import Division

class Calculator:
    """ Creating a Module Calculator """
    # result set to 0 for initialization
    history = []

    @staticmethod
    def clear_history():
        """ Clear the history array """
        Calculator.history.clear()
        return True

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Appends calculation to history array """
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_first_calculation_history():
        """ Gets first calculation from history array """
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation_added():
        return Calculator.history[-1]

    @staticmethod
    def add_nums(value_a, value_b):
        """ Adds given number and appends the result to history """
        addition = Addition.create(value_a, value_b)
