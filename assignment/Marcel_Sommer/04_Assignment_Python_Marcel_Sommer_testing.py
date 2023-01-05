import math
import unittest


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1]

def decimal_to_binary_correct(n):
    # function to convert decimal integers to binary
    y = []
    if n > 0:
        while n > 0:
            y.append(n % 2)
            n = math.floor(n/2)
    elif n == 0:
        y=[0, 0, 0, 0]
    else:
        while abs(n) > 0:
            y.append(abs(n) % 2)
            n = math.floor(abs(n)/2)
        while len(y) < 4:
            y.append(0)
        y.append(1)
    return y[::-1]



class Unit_test(unittest.TestCase):
    """Tests for 'decimal2binary'."""

    def test_minus_one(self):
        decimal = decimal_to_binary_correct(-1)
        self.assertEqual(decimal,[1, 0, 0, 1])

    def test_zero(self):
        decimal = decimal_to_binary_correct(0)
        self.assertEqual(decimal, [0, 0, 0, 0])

    def test_one(self):
        decimal = decimal_to_binary_correct(1)
        self.assertEqual(decimal, [1])

    def test_two(self):
        decimal = decimal_to_binary_correct(2)
        self.assertEqual(decimal, [1, 0])

    def test_three(self):
        decimal = decimal_to_binary_correct(3)
        self.assertEqual(decimal, [1, 1])

if __name__ == '__main__':
    unittest.main()
