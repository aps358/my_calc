"""Importing Calculator Class from calculator > main.py for Testing"""

from calculator.main import Calculator


def test_calculator_result():
    """ To check if calculator initial result is 0 """
    calc_obj = Calculator()
    assert calc_obj.get_result() == 0

def test_calculator_add():
    """ To check if calculator addition result is correct """
    calc_obj = Calculator()
    calc_obj.addition(10, 20)
    assert calc_obj.get_result() == 30

def test_calculator_subtract():
    """ To check if calculator subtraction result is correct """
    calc_obj = Calculator()
    calc_obj.subtraction(10, 20)
    assert calc_obj.get_result() == -10

def test_calculator_multiply():
    """ To check if calculator multiplication result is correct """
    calc_obj = Calculator()
    calc_obj.multiplication(10, 20)
    assert calc_obj.get_result() == 200

def test_calculator_divide():
    """ To check if calculator division result is correct"""
    calc_obj = Calculator()
    calc_obj.division(20, 10)
    assert calc_obj.get_result() == 2
