"""CSV Manager Testing"""
import string
import logging
import pandas as pd

class CsvReader:
    """The file handle in the code is managed by the CSV Reader class"""
    @staticmethod
    def get_data_frame_from_csv_division(division: string): # pylint: disable =unused-argument,
        # redefined-outer-name
        """Obtain the division data and return it"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\division.csv")

    @staticmethod
    def get_data_frame_from_csv_multiplication(multiplication: string): # pylint: disable =unused-argument,
        # redefined-outer-name
        """Get the multiplication information and return it"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\
        multiplication.csv")

    @staticmethod
    def get_data_frame_from_csv_addition(addition: string): # pylint: disable =unused-argument,
        # redefined-outer-name
        """Get addition information and return"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\addition.csv")

    @staticmethod
    def get_data_frame_from_csv_subtraction(subtraction: string): # pylint: disable =unused-argument,
        # redefined-outer-name
        """Get subtraction information and return it"""
        return pd.read_csv(r"C:\Users\Sabina\PycharmProjects\project3\tests\test_data\
        subtraction.csv")

# This reflects the log portion of the code
logging.root.handlers = []
logging.basicConfig(format='%(created)f : : %(name)s : %(levelname)s : %(message)s'
                    , level=logging.INFO, filename=r"C:\Users\Sabina\PycharmProjects\project3\
                    results\results.log")
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
