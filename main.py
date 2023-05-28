from file_functions import FileWorker
from data_functions import SumOfPairs

def run_application(path_to_file, location_to_save, save_data=True):
    """
    Use created classes to read the data from the file and go through the logic (find pairs of numbers that are equal 12)
    :return: saved file
    """
    try:
        # Read the data from the text file
        data_reader = FileWorker()
        list_of_numbers = data_reader.load_data(path_to_file)

        # Initialize main logic
        pairs_of_numbers = SumOfPairs(list_of_numbers)

        # Check the input (data validation)
        data_check = pairs_of_numbers.validation()

        # If there is no returned value then we can proceed to the point where we create pairs of numbers
        if data_check is None:
            result = str(pairs_of_numbers.find_pairs())
            if save_data is True:
                data_reader.save_data(location_to_save, result)

            print(f'List of pairs: {result}')
            return result
        else:
            print(data_check)

    except Exception as e:
        print(e)


path_to_file = r"location_with_entry_file"
location_to_save = r"location_where_the_results_will_be_saved"

if __name__ == '__main__':
    run_application(path_to_file, location_to_save)