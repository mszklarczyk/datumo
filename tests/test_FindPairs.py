from unittest import TestCase
from collections import Counter
from FindPairs import FindPairs


class TestFindPairs(TestCase):
    tmp_list1 = [0, 0, 0, 0, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]
    tmp_list2 = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
    test_input1 = FindPairs(tmp_list1, 12)
    test_input2 = FindPairs(tmp_list2, 12)
    test_input3 = FindPairs(tmp_list1, 13)
    test_input4 = FindPairs(tmp_list2, 13)

    def test_populate_input_dict(self):
        result = self.test_input1.populate_input_dict()
        awaited_result = {0: 4, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2}
        self.assertEqual(result, awaited_result)
        result = self.test_input2.populate_input_dict()
        awaited_result = {4: 4, 12: 4, 8: 2, 0: 2, 9: 1, 1: 1, 2: 1, 11: 1}
        self.assertEqual(result, awaited_result)

    def test_find_pairs(self):
        result = self.test_input1.find_pairs(Counter({0: 4, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2}))
        awaited_result = {(0, 12): 2, (2, 10): 2, (3, 9): 2, (4, 8): 2, (5, 7): 2, (6, 6): 1}
        self.assertEqual(result, awaited_result)
        result = self.test_input2.find_pairs(
            Counter({4: 4, 12: 4, 8: 2, 0: 2, 9: 1, 1: 1, 2: 1, 11: 1}))
        awaited_result = {(0, 12): 2, (1, 11): 1, (4, 8): 2}
        self.assertEqual(result, awaited_result)
        result = self.test_input3.find_pairs(
            Counter({0: 4, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2}))
        awaited_result = {(2, 11): 2, (3, 10): 2, (4, 9): 2, (5, 8): 2, (7, 6): 2}
        self.assertEqual(result, awaited_result)
        result = self.test_input4.find_pairs(
            Counter({4: 4, 12: 4, 8: 2, 0: 2, 9: 1, 1: 1, 2: 1, 11: 1}))
        awaited_result = {(1, 12): 1, (2, 11): 1, (4, 9): 1}
        self.assertEqual(result, awaited_result)
