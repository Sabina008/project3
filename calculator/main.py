"""CSV Manager Testing"""
import string
import pandas as pd
import logging

class CsvReader:
    """The file handle in the code is managed by the CSV Reader class"""
    @staticmethod
    def get_data_frame_from_csv_addition(addition: string):
        """Get addition information and return"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\addition.csv")

    @staticmethod
    def get_data_frame_from_csv_subtraction(subtraction: string):
        """Get subtraction information and return it"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\subtraction.csv")

    @staticmethod
    def get_data_frame_from_csv_multiplication(multiplication: string):
        """Get the multiplication information and return it"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\multiplication.csv")

    @staticmethod
    def get_data_frame_from_csv_division(division: string):
        """Obtain the division data and return it"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\division.csv")

# This reflects the log portion of the code
logging.root.handlers = []
logging.basicConfig(format='%(created)f : : %(name)s : %(levelname)s : %(message)s'
                    , level=logging.INFO, filename=r"C:\Users\Sabina\PycharmProjects\project3\results\results.log")
# Console set up log
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
# Unix Timestamp Format
formatter = logging.Formatter('%(created)f : %(name)s :  %(levelname)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.exception('exp')
