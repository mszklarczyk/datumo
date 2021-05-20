from unittest import TestCase
from OutputGenerate import OutputGenerate


class Test(TestCase):
    dict1 = {(0, 12): 2, (2, 10): 2, (3, 9): 2, (4, 8): 2, (5, 7): 2, (6, 6): 1}
    test_input1 = OutputGenerate(dict1, '', 'list')
    dict2 = {(0, 12): 2, (1, 11): 1, (4, 8): 2}
    test_input2 = OutputGenerate(dict2, '', 'list')

    def test_populate_out_list(self):
        result = self.test_input1.out_list
        awaited_result = [(0, 12), (0, 12), (2, 10), (2, 10), (3, 9), (3, 9), (4, 8), (4, 8), (5, 7), (5, 7), (6, 6)]
        self.assertEqual(result, awaited_result)
        result = self.test_input2.out_list
        awaited_result = [(0, 12), (0, 12), (1, 11), (4, 8), (4, 8)]
        self.assertEqual(result, awaited_result)


