"""Testing the CSV Reader"""
from calculator.main import CsvReader

def test_get_data_frame_from_csv_division():
    """CSV Reader division testing"""
    data = CsvReader()
    result = data.get_data_frame_from_csv_division()
    assert True

def test_get_data_frame_from_csv_multiplication():
    """Multiplication CSV Reader Testing"""
    data = CsvReader()
    result = data.get_data_frame_from_csv_multiplication()
    assert True

def test_get_data_frame_from_csv_addition():
    """Addition CSV Reader Testing"""
    data = CsvReader()
    result = data.get_data_frame_from_csv_addition()
    assert True

def test_get_data_frame_from_csv_subtraction():
    """Subtraction CSV Reader Testing"""
    data = CsvReader()
    result = data.get_data_frame_from_csv_subtraction()
    assert True








