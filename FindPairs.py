from collections import Counter
from collections import defaultdict


class FindPairs:
    """
    A class to represent an algorithm object finding pairs from given input.

    Attributes
    ----------
    input_list : list
        List containing numbers for further processing
    total_sum : int
        Sum for which algorithm is looking for pairs

    Methods
    -------
    populate_input_dict():
        Convert 'input_list' to Counter object containing numbers as keys and theirs frequency in 'input_list' as values.
    find_pairs(input_dict):
        Algorithm implementation for finding pairs from given list of numbers which sum == 'total_sum'
    """
    def __init__(self, input_list, total_sum):
        """
        Constructs all the necessary attributes for the algorithm object.

        Parameters
        ----------
        input_list : list
            List containing numbers for further processing
        total_sum : int
            Sum for which algorithm is looking for pairs
        """
        self.input_list = input_list
        self.total_sum = total_sum

    def populate_input_dict(self):
        """
        Convert 'input_list' to Counter object containing numbers as keys and theirs frequency in 'input_list' as values.

        Return
        ----------
        input_dict : Counter
            Dictionary type object containing numbers as keys ant their frequency in 'input_list'
        """
        input_dict = Counter(self.input_list)
        return input_dict

    def find_pairs(self, input_dict):
        """
        Algorithm implementation for finding pairs from given list of numbers which sum == 'total_sum'

        Parameters
        ----------
        input_dict : Counter
            Dictionary type object containing numbers as keys ant their frequency in 'input_list'

        Return
        ----------
        out_dict : dict
            Dictionary holds tuples of number pairs as keys and integer as value
        """
        midpoint = self.total_sum // 2
        out_dict = defaultdict(int)
        for k in range(midpoint):
            pair_tuple = (k, self.total_sum - k)
            out_dict[pair_tuple] = min(input_dict[k], input_dict[self.total_sum - k])

        # handle the middle of the compartment
        if self.total_sum % 2 == 0 and input_dict.__contains__(midpoint):
            out_dict[(midpoint, midpoint)] = input_dict[midpoint] // 2
        elif self.total_sum % 2 == 1:
            midpoint += 1  # corrected midpoint for odd length
            pair_tuple = (midpoint, self.total_sum - midpoint)
            out_dict[pair_tuple] = min(input_dict[midpoint], input_dict[self.total_sum - midpoint])
        else:
            None    # handled in lines 17-19

        # delete dictionary items with 0 value
        out_dict = dict(filter(lambda x: x[1] != 0, out_dict.items()))
        return out_dict
