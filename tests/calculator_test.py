# Importing Calculator Class from calculator > main.py for Testing

from calculator.main import Calculator

# To check if calculator initial result is 0
def test_calculator_result():
    # Creating Calculator Object
    calc_obj = Calculator()
    assert calc_obj.get_result() == 0

# To check if calculator addition result is correct
def test_calculator_add():
    calc_obj = Calculator()
    calc_obj.addition(10, 20)
    assert calc_obj.get_result() == 30

# To check if calculator subtraction result is correct
def test_calculator_subtract():
    calc_obj = Calculator()
    calc_obj.subtraction(10, 20)
    assert calc_obj.get_result() == -10

# To check if calculator multiplication result is correct
def test_calculator_multiply():
    calc_obj = Calculator()
    calc_obj.multiplication(10, 20)
    assert calc_obj.get_result() == 200

# To check if calculator division result is correct
def test_calculator_divide():
    calc_obj = Calculator()
    calc_obj.division(20, 10)
    assert calc_obj.get_result() == 2
