import unittest
import math

def decimal_to_binary_correct(n):
    # function to convert decimal integers to binary
    x = []
    if n < 0:
        while abs(n) > 0:
            x.append(abs(n) % 2)
            n = math.floor(abs(n)/2)
        while len(x) < 3:
            x.append(0)
        x.append(1)
    elif n == 0:
        while len(x) < 4:
            x.append(0)
    else:
        while n > 0:
            x.append(n % 2)
            n = math.floor(n/2)
    return x[::-1]


class UnitTest(unittest.TestCase):

    def test_minus_one(self):
        number_obj = -1
        binary_number = decimal_to_binary_correct(number_obj)
        self.assertEqual(binary_number, [1, 0, 0, 1])

    def test_zero(self):
        number_obj = 0
        binary_number = decimal_to_binary_correct(number_obj)
        self.assertEqual(binary_number, [0, 0, 0, 0])

    def test_one(self):
        number_obj = 1
        binary_number = decimal_to_binary_correct(number_obj)
        self.assertEqual(binary_number, [1])

    def test_two(self):
        number_obj = 2
        binary_number = decimal_to_binary_correct(number_obj)
        self.assertEqual(binary_number, [1, 0])

    def test_three(self):
        number_obj = 3
        binary_number = decimal_to_binary_correct(number_obj)
        self.assertEqual(binary_number, [1, 1])

if __name__ == '__main__':
    unittest.main()
