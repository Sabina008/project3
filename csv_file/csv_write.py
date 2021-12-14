""" CSV write class"""
import os
import pandas as pd
# pylint: disable=too-few-public-methods


class CsvWriter:
    """This class is to write the csv file"""
    @staticmethod
    def data_frame_csv_file_write(filename, df):
        """Function to read a csv file and return values"""
        return df.to_csv(os.path.abspath(filename), float_format='%.2f', index=True, header=True)
