"""Importing Calculator Class from calculator > main.py for Testing"""
import pprint
import pytest
from calculator.main import Calculator


# This is called a fixture and it runs each time you pass it to a test
@pytest.fixture
def clear_history():
    Calculator.clear_history()


def test_calculator_add(clear_history):
    """ To check if calculator addition result is correct """
    assert Calculator.add_nums(10, 20) == 30
    assert Calculator.get_calculation_count() == 1
    pprint.pprint(Calculator.history)

# def test_calculator_subtract():
#     """ To check if calculator subtraction result is correct """
#     calc_obj = Calculator()
#     calc_obj.subtraction(10, 20)
#     assert calc_obj.get_result() == -10
#
# def test_calculator_multiply():
#     """ To check if calculator multiplication result is correct """
#     calc_obj = Calculator()
#     calc_obj.multiplication(10, 20)
#     assert calc_obj.get_result() == 200
#
# def test_calculator_divide():
#     """ To check if calculator division result is correct"""
#     calc_obj = Calculator()
#     calc_obj.division(20, 0)
#     assert calc_obj.get_result() == 2
