import json


class InputPrepare:
    """
    A class to represent an input data from input file and populate them to list.

    Attributes
    ----------
    filename : str
        Path to file with input data containing list with numbers

    Methods
    -------
    read_file():
        Read data from given file.
    load_data_2list():
        Convert raw string to list of int.

    Raises
    ------
    FileNotFoundError
        If input file don't exist
    ValueError
        If input data in filename is in wrong format, expected list of numbers [0, 1, 2, 3]
    """

    def __init__(self, filename):
        """
        Constructs all the necessary attributes for the input data object.

        Parameters
        ----------
            filename : str
                Path to file with input data containing list with numbers
        """
        self.filename = filename

    def read_file(self):
        """
        Read data from given file.

        Return
        ----------
        content : str
            Raw string extracted from input file
        """
        try:
            with open(self.filename) as f:
                content = f.readline()
            return content
        except FileNotFoundError:
            raise FileNotFoundError("Input file don't exist")

    def load_data_2list(self):
        """
        Convert raw string to list of int.

        Return
        ----------
        input_list : list
            List containing numbers for further processing
        """
        try:
            input_list = json.loads(self.read_file())
        except json.decoder.JSONDecodeError:
            raise ValueError('Input data in wrong format, expected list of numbers [0, 1, 2, 3]')
        return input_list

