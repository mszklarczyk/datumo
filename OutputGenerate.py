import json


def populate_out_list(out_dict):
    """
    Method for converting dictionary to list containing out_dict keys repeated out_dict[key] times.

    Parameters
    ----------
    out_dict: dict
        Dictionary holds tuples of number pairs as keys and integer as value

    Returns
    ----------
    out_list : list
        List of two element lists (number pairs)
    """
    out_list = []
    for k in out_dict.keys():
        for v in range(out_dict[k]):
            out_list.append(k)
    return out_list


class OutputGenerate:
    """
    A class to represent an output data and write them to file.

    Attributes
    ----------
    out_data : dict
        Dictionary holds tuples of number pairs as keys and integer as value
    filename : str
        Path to file where results will be saved
    output_type : str
        Define type of output data writen in file, allowed values: list or dict
    out_list : list
        List of two element lists (number pairs)

    Methods
    -------
    write_2file():
        Write data to given file.

    Raises
    ------
    ValueError
        If 'output_type' not in ['list','dict']
    """

    def __init__(self, out_data, filename, output_type):
        """
        Constructs all the necessary attributes for the output data object.

        Parameters
        ----------
            out_data : dict
                Dictionary holds tuples of number pairs as keys and integer as value
            filename : str
                Path to file where results will be saved
            output_type : str
                Define type of output data writen in file, allowed values: list or dict
        """
        self.out_data = out_data
        self.output_type = output_type
        self.filename = filename
        self.out_list = populate_out_list(out_data)

    def write_2file(self):
        """
        Write data to given file. Output format depends on 'output_type' value.
        """
        if self.output_type == 'list':
            self.out_data = populate_out_list(self.out_data)
            with open(self.filename, "w") as f:
                json.dump(self.out_data, f)
        elif self.output_type == 'dict':
            with open(self.filename, 'w') as f:
                json.dump({str(k): v for k, v in self.out_data.items()}, f)
        else:
            raise ValueError('Parameter output_type={} unknown'.format(self.output_type))

