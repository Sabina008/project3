import pandas as pd

class Read:
    @staticmethod
    def DataFrameFromCSVFile(filename):
        return pd.read.csv(filename)
