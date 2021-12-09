"""Calculator Testing"""
from calculator.calculator import Calculator


def test_calculator_result():
    """Calculator testing result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Addition function testing of the calculator"""
    calc = Calculator()
    result = calc.add_numbers(6,3)
    assert result == 9

def test_calculator_get_result():
    """Get result method testing of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Subtract method testing of the calculator"""
    calc = Calculator()
    result= calc.subtract_numbers(3,8)
    assert result == -5

def test_calculator_multiply():
    """Multiplication method testing of the calculator"""
    calc = Calculator()
    result = calc.multiply_numbers(6,3)
    assert result == 18

def test_calculator_divide_by_zero():
    """Division method testing of the calculator by two numbers with denominator zero"""
    calc = Calculator()
    result = calc.divide_numbers(2,0)
    assert result is None

def test_calculator_divide():
    """Division method testing of the calculator of two numbers"""
    calc = Calculator()
    result = calc.divide_numbers(9,3)
    assert result == 3
