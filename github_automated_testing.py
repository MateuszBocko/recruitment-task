import os
import pytest
import ast 

from main import run_application, location_to_save
from file_functions import FileWorker

testing_pairs = [
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_empty.txt', []),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_natural_numbers_1.txt', []),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_natural_numbers_2.txt', [(0, 12)]),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_natural_numbers_3.txt', [(0, 12), (1, 11), (2, 10)]),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_natural_numbers_4.txt', [(4, 8)]),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_natural_numbers_5.txt', [(5, 7)]),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_only_negative_numbers.txt', []),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_negative_and_natural_numbers.txt', [(1, 11)]),
    ('/home/runner/work/Datumo/Datumo/data/test_data/test_string_as_input.txt', [(1, 11), (0, 12)]),
    ('/home/runner/work/Datumo/Datumo/data/test_data/mixed_incorrect_formats.txt', [(0, 12), (1, 11), (1, 11), (2, 10), (6, 6)])
]

def test_run_app(test_input,expected):
    """
    Test application using multiple input files.
    :param test_input: text file with input data
    :param expected: expected result of application output
    """
    result = run_application(test_input, location_to_save, save_data=False)
    result = ast.literal_eval(result)
    assert sorted(result) == sorted(expected)

if __name__ == '__main__':
    test_number = 1
    for input_data, expected_result in testing_pairs:
        data_reader = FileWorker()
        list_of_numbers = data_reader.load_data(input_data)
        print(f'''\nTest: {test_number} \nInput list: {list_of_numbers} \nExpected return: {expected_result}''')
        test_run_app(input_data, expected_result)
        test_number += 1
