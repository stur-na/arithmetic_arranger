import unittest
from arithmetic_arranger import arithmetic_arranger

class arithmetictest(unittest.TestCase):

    def test_arrangement(self):
        actual = arithmetic_arranger([
            '12 + 2345', '2 - 2453', '3433 + 456', '4333 - 65', '109 + 1'
        ])
        expected = '    12         2      3433      4333      109\n+ 2345    - 2453    +  456    -   65    +   1\n------    ------    ------    ------    -----'
        self.assertEqual(actual, expected)

    def too_many_problems(self):
        actual = arithmetic_arranger([
            '12 + 2345', '2 - 253', '3433 + 456', '4333 - 65', '109 + 1', '12 - 10'
        ])
        expected = 'Error: Too many problems.'
        self.assertEqual(actual, expected)

    def test_only_digits(self):
        actual = arithmetic_arranger([
            '12i - 10', '122 + 34', '232 - 2', '33 - 10', '2 - 1'
        ])
        expected = 'Error: Numbers must only contain digits.'
        self.assertEqual(actual, expected)

    def test_operator(self):
        actual = arithmetic_arranger([
            '234 / 34', '34 - 3', '876 + 23', '1 - 1', '444 + 2'
        ])
        expected = 'Error: Operator must be "+" or "-".'
        self.assertEqual(actual, expected)

    def test_number_of_digits(self):
        actual = arithmetic_arranger([
            '23433 - 3', '3462 + 234', '3546 - 2', '10 + 10', '234 - 12'
        ])
        expected = 'Error: Numbers cannot be more than four digits.'
        self.assertEqual(actual, expected)

    def test_results(self):
        actual = arithmetic_arranger(['12 + 2345', '2 - 2453', '3433 + 456', '4333 - 65', '109 + 1'], True)
        expected = '    12         2      3433      4333      109\n+ 2345    - 2453    +  456    -   65    +   1\n------    ------    ------    ------    -----\n  2357     -2451      3889      4268      110'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()