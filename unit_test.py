import os
import pytest
import ast

from main import run_application, location_to_save

def clean_location():
    """
    Remove file saved at the end of application running for testing purposes
    """
    path = os.path.join(location_to_save, "result.txt")
    os.remove(path)

def check_location():
    """
    Check if application saved results in provided location
    """
    file_to_find = "result.txt"
    directory_with_output = os.listdir(location_to_save)
    assert file_to_find in directory_with_output

@pytest.mark.parametrize('test_input,expected', [
    (r'data\test_data\test_empty.txt', []),
    (r'data\test_data\test_natural_numbers_1.txt', []),
    (r'data\test_data\test_natural_numbers_2.txt', [(0, 12)]),
    (r'data\test_data\test_natural_numbers_3.txt', [(0, 12), (1, 11), (2, 10)]),
    (r'data\test_data\test_natural_numbers_4.txt', [(4, 8)]),
    (r'data\test_data\test_natural_numbers_5.txt', [(5, 7)]),
    (r'data\test_data\test_only_negative_numbers.txt', []),
    (r'data\test_data\test_negative_and_natural_numbers.txt', [(1, 11)]),
    (r'data\test_data\test_string_as_input.txt', [(1, 11), (0, 12)]),
    (r'data\test_data\mixed_incorrect_formats.txt', [(0, 12), (1, 11), (1, 11), (2, 10), (6, 6)])
])

def test_run_app(test_input,expected):
    """
    Test application using multiple input files.
    :param test_input: text file with input data
    :param expected: expected result of application output
    """
    result = run_application(test_input, location_to_save)
    result = ast.literal_eval(result)
    assert sorted(result) == sorted(expected)
    check_location()
    clean_location()

