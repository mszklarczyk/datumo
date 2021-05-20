import random


def generate_test_data(quantity, max_num, output_file):
    """
    Method to generate random numbers and save to .txt file.

    Parameters
    ------
    quantity : int
        Value of generated numbers
    max_num : int
        Upper limit for random number generator
    output_file : str
        Path and file suffix for output data

    Returns
    ------
    None
    """
    random_list = []
    for i in range(0, quantity):
        n = random.randint(0, max_num)
        random_list.append(n)
    filename = "".join([output_file, str(quantity), '.txt'])

    with open(filename, 'w') as f:
        f.writelines(str(random_list))


if __name__ == '__main__':
    generate_test_data(10, 12, 'data/data')
