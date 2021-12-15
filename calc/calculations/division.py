"""Child Class = Division Class"""
import pprint

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division calculation object"""
    def get_result(self):
        """get the Division results"""
        result = 1.0
        for value in self.values:
            result = result / value
        return result
