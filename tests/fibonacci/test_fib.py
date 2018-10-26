import types
import unittest
from collections import deque

from exercises.fibonacci.fib import generate_fibonacci


class FibonacciTests(unittest.TestCase):
    def test_fibonacci_short(self):
        sequence = generate_fibonacci(10)
        self.assertTrue(isinstance(sequence, types.GeneratorType))

        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, number in enumerate(sequence):
            self.assertEqual(number, expected[i])

    def test_fibonacci_large(self):
        sequence = generate_fibonacci(100)
        self.assertTrue(isinstance(sequence, types.GeneratorType))

        last = deque(sequence, maxlen=1)[0]
        expected = 218922995834555169026
        self.assertEqual(last, expected)
