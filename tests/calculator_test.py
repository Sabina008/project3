"""Testing the Calculator"""
from calculator.calculator import Calculator


def test_calculator_result():
    """Testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    result = calc.add_numbers(4,2)
    assert result == 6

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    result= calc.subtract_numbers(4,7)
    assert result == -3

def test_calculator_multiply():
    """Testing multiplication of two numbers"""
    calc = Calculator()
    result = calc.multiply_numbers(4,3)
    assert result == 12

def test_calculator_divide_by_zero():
    """Testing division by two numbers with denominator zero"""
    calc = Calculator()
    result = calc.divide_numbers(4,0)
    assert result is None

def test_calculator_divide():
    """Testing division of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(4,2)
    assert result == 2
