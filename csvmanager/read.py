"""Testing Read CSV file """
import os
import pandas as pd

class Read:
    """This is the Read Class used for reading """
    # pylint: disable=too-few-public-methods
    @staticmethod
    def dataframefromcsvfile(filename):
        """static method returns file path """
        return pd.read_csv(os.path.abspath(filename))
