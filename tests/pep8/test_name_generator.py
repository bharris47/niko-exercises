import random
import unittest

from exercises.pep8.name_generator import getRandomName


class NameGeneratorTests(unittest.TestCase):
    def test_get_random_name(self):
        name = getRandomName(1)
        expected = 'Bob Smith'
        self.assertEqual(name, expected)
