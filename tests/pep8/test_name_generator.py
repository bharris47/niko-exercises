import random
import unittest

from exercises.pep8.name_generator import get_random_name


class NameGeneratorTests(unittest.TestCase):
    def test_get_random_name(self):
        random.seed(1)
        name = get_random_name()
        expected = 'Alice Harris'
        self.assertEqual(name, expected)
