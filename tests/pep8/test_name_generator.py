import random
import unittest

from exercises.pep8.name_generator import getRandomName


class NameGeneratorTests(unittest.TestCase):
    def test_get_random_name(self):
        random.seed(1)
        name = getRandomName()
        expected = 'Alice Harris'
        self.assertEqual(name, expected)
