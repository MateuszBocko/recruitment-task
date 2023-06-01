import ast
import os

class FileWorker:
    def load_data(self, path_to_file):
        """
        A function that will read the data.
        :param path_to_file: path to the file with data
        :return: list with numbers
        """
        with open(path_to_file) as f:
            lines = f.readlines()
            list_of_numbers = ast.literal_eval(lines[0])

        return list_of_numbers

    def save_data(self, location_to_save, result):
        """
        A function that saves output in text file in provided location
        :param location_to_save: path to save location
        :param result: output that will be saved
        """
        path = os.path.join(location_to_save, "result.txt")

        with open(path, 'w') as f:
            f.write(result)
