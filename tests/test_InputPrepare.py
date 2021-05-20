from unittest import TestCase
from InputPrepare import InputPrepare


class TestInputPrepare(TestCase):
    test_input1 = InputPrepare('../data/data.txt')
    test_input2 = InputPrepare('../data/data1.txt')

    def test_load_data_2list(self):
        result = self.test_input1.load_data_2list()
        awaited_result = [0, 0, 0, 0, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
        self.assertEqual(result, awaited_result)
        result = self.test_input2.load_data_2list()
        awaited_result = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
        self.assertEqual(result, awaited_result)

