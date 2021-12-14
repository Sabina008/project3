""" CSV read class"""
import pandas as pd
# pylint: disable=too-few-public-methods


class CsvReader:
    """This class is to read the csv file"""
    @staticmethod
    def data_frame_csv_file_read(filename):
        """Function to read a csv file and return values"""
        return pd.read_csv(filename)
