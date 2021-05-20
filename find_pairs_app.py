from FindPairs import FindPairs
from InputPrepare import InputPrepare
from OutputGenerate import OutputGenerate
import sys


def find_pairs_app(filename, output_type, total_sum, output_file):
    """
    Main method to find pairs from given list located in input file.

    Parameters
    ------
    filename : str
        Path to file with input data containing list with numbers
    output_type : str
        Define type of output data writen in file, allowed values: list or dict
    total_sum : int
        Sum for which algorithm is looking for pairs
    output_file : str
        Path to file with output data, output data type depends on output_type param

    Returns
    ------
    None

    Raises
    ------
    FileNotFoundError
        If input file don't exist
    ValueError
        If input data in filename is in wrong format, expected list of numbers [0, 1, 2, 3]
    ValueError
        If 'output_type' not in ['list','dict']
    IndexError
        If missing parameter

    Example
    -------
    $ python find_pairs_app.py data/data.txt dict 12 data/result.txt
    """
    input_list = InputPrepare(filename).load_data_2list()
    pairs = FindPairs(input_list, total_sum)
    input_dict = pairs.populate_input_dict()
    algorithm_result_dict = pairs.find_pairs(input_dict)
    output_results = OutputGenerate(algorithm_result_dict, output_file, output_type)
    output_results.write_2file()


if __name__ == '__main__':
    try:
        find_pairs_app(filename=sys.argv[1], output_type=sys.argv[2], total_sum=int(sys.argv[3]), output_file=sys.argv[4])
    except IndexError:
        print("""sample usage:
        $ find_pairs_app.py data_file output_type total_sum output_file
        data_file    - path to file with input data
        output_type  - allowed values: list or dict
        total_sum    - sum for which we are looking for pairs 
        output_file  - path to file with output data
        
        Example:
        $ find_pairs_app.py data/data.txt dict 12 data/result.txt
        """)
