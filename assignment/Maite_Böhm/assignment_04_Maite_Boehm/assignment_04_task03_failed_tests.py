import unittest
import math


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1]

class Unit_test(unittest.TestCase):


    def test_minus_one(self):
        number_obj = -1
        binary_number = decimal2binary(number_obj)
        self.assertEqual(binary_number, [1, 0, 0, 1])

    def test_zero(self):
        number_obj = 0
        binary_number = decimal2binary(number_obj)
        self.assertEqual(binary_number, [0])

    def test_one(self):
        number_obj = 1
        binary_number = decimal2binary(number_obj)
        self.assertEqual(binary_number, [1])

    def test_two(self):
        number_obj = 2
        binary_number = decimal2binary(number_obj)
        self.assertEqual(binary_number, [1, 0])

    def test_three(self):
        number_obj = 2
        binary_number = decimal2binary(number_obj)
        self.assertEqual(binary_number, [1, 1])

if __name__ == '__main__':
    unittest.main()
