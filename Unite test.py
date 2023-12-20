import unittest

def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1, "Factorial of 0 should be 1")

    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1, "Factorial of 1 should be 1")

    def test_factorial_of_positive_integer(self):
        self.assertEqual(factorial(5), 120, "Factorial of 5 should be 120")

    def test_factorial_of_large_number(self):
        self.assertEqual(factorial(10), 3628800, "Factorial of 10 should be 3628800")

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == '__main__':
    unittest.main()
