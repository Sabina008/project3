"""This file reflects the increment function"""

class Calculator:
    """This reflects the Calculator class"""

    result = 0

    def get_result(self):
        """This reflects the Get Result of Calculation"""
        return self.result

    def add_numbers(self, value_1, value_2):
        """This reflects the Addition of two value_2ers and store the result"""
        self.result = value_1 + value_2
        return self.result

    def subtract_numbers(self, value_1, value_2):
        """This reflects the Subtraction of two value_2ers and store the result"""
        self.result = value_1 - value_2
        return self.result

    def multiply_numbers(self, value_1, value_2):
        """This reflects the Multiplication of two value_2ers and store the result"""
        self.result = value_1 * value_2
        return self.result

    def divide_numbers(self, value_1, value_2):
        """This reflects the Division of two value_2ers and store the result"""
        try:
            self.result = value_1 / value_2

        except ZeroDivisionError:
            return None
        else:
            return self.result
