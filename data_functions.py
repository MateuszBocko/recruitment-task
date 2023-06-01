import ast

class SumOfPairs():
    def __init__(self, list_of_numbers):
        self.sum_of_numbers = 12
        self.list_of_numbers = list_of_numbers
        self.clean_list_of_numbers = []
        self.list_of_removed_numbers = []

    def type_check(self):
        """
        A function that checks input data format. If data type is tuple it will be converted to list.
        :return: Data input as list
        """
        if type(self.list_of_numbers) is list:
            pass
        elif type(self.list_of_numbers) is tuple:
            self.list_of_numbers = list(self.list_of_numbers)
        else:
            return 'Data input is invalid! Provided data format should be as following: [number, number, number]'

    def input_check(self):
        """
        A function that will check each element of the list, if it is a natural number or not.
        If it is a float or a number in string type, then convert it to integer.
        :return:
        """
        # check if all elements in list are natural numbers
        is_int = all(isinstance(x, int) for x in self.list_of_numbers)
        if is_int is True:
            self.clean_list_of_numbers = self.list_of_numbers
        else:
            # iterate over each element and check if it can be converted to integer
            for element in self.list_of_numbers:
                if type(element) == int:
                    self.clean_list_of_numbers.append(element)
                elif type(element) != int:
                    self.not_int_type(element)

    def not_int_type(self, element):
        """
        Sub function to input_check function. Here the code is handling only non integers elements.
        :param element: non integer element
        :return:
        """
        try:
            converted_element = int(element)
            self.clean_list_of_numbers.append(converted_element)
        except ValueError:
            try:
                converted_element = int(float(element))
                self.clean_list_of_numbers.append(converted_element)
            except:
                self.list_of_removed_numbers.append(element)
    def numbers_check(self):
        """
        A function that removes any number that is bigger than 12 or is negative
        """
        # We assign the list of numbers after first cleanse to the old list, so we can iterate over it again
        self.list_of_numbers = self.clean_list_of_numbers.copy()
        self.clean_list_of_numbers = []

        for number in self.list_of_numbers:
            if number > 12 or number < 0:
                self.list_of_removed_numbers.append(number)
            else:
                self.clean_list_of_numbers.append(number)

    def validation(self):
        """
        A function that combine validation of data type and numbers
        :return: Error message or nothing
        """
        type_check = self.type_check()
        if type_check is None:
            self.input_check()
            self.numbers_check()
        else:
            return type_check

    def find_pairs(self):
        """
        A function to find pairs of numbers that are equal to a specified value.
        :param list_of_numbers: list with numbers
        :param sum_of_numbers: value to be achieved
        :return: List of pairs
        """
        self.clean_list_of_numbers.sort()
        result = []

        while self.clean_list_of_numbers:
            num = self.clean_list_of_numbers.pop()
            diff = self.sum_of_numbers - num

            if diff in self.clean_list_of_numbers:
                result.append((diff, num))
                self.clean_list_of_numbers.pop(self.clean_list_of_numbers.index(diff))

        return result
