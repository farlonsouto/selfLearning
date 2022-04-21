import unittest

from MathProblem import MathProblem as SortWith


class BubbleSortTest(unittest.TestCase):
    """ Will cover the bubble sort implementation with some simple test cases"""

    def test_empty_list(self):
        original = []
        SortWith.bubbleSort(original)
        self.assertEqual(original, [])

    def test_None(self):
        with self.assertRaises(ValueError):
            SortWith.bubbleSort(None)

    def test_already_sorted_inputs(self):
        original = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertExpected(original, expected)

    def test_all_negative_inputs(self):
        original = [-1, -2, -3]
        expected = [-3, -2, -1]
        self.assertExpected(original, expected)

    def test_simple_inputs(self):
        original = [1, 5, 3, 4, 2]
        expected = [1, 2, 3, 4, 5]
        self.assertExpected(original, expected)

    def test_group_by(self):
        original = [1, 1, 5, 3, 4, 2, 5, 5, 5, 3, 4, 2, 2, 2, 2]
        expected = [1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5]
        self.assertExpected(original, expected)

    def assertExpected(self, original, expected):
        """ Helper method that implements the common assertion approach.
            Args:
                original: the original list populated with values.
                expected: the expected list after the sorting is applied."""
        SortWith.bubbleSort(original)
        for i in range(len(original)):
            self.assertEqual(original[i], expected[i])  # add assertion here


if __name__ == '__main__':
    unittest.main()
