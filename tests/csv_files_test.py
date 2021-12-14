""" Testing the CSV file management read and write"""
import os.path
import pandas
import pandas as pd
from csv_file.csv_read import CsvReader
from csv_file.csv_write import CsvWriter


def test_writing_to_csv():
    """This is a test for our calculator for addition"""
    # Arrange
    filename = 'results.csv'
    path = 'tests/test_data'
    full_path = path + '/' + filename
    dict_name = {'num1': ['3.0', '6.0', '1.0'],
                 'num2': ['5.0', '4.0', '2.0'],
                 'result': [8.0, 10.0, 3.0]}

    df = pd.DataFrame(dict_name)

    # Act
    CsvWriter.data_frame_csv_file_write(full_path, df)

    # Assert
    assert os.path.exists(full_path)


def test_reading_from_csv():
    """This is a test for our calculator for addition"""
    # Arrange
    filename = 'results.csv'
    path = 'tests/test_data'
    full_path = path + '/' + filename

    # Act
    df = CsvReader.data_frame_csv_file_read(full_path)

    # Assert
    assert type(df) is pandas.DataFrame
