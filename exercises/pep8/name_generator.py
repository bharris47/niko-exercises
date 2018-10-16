#!/usr/bin/env python
""" bitch
"""
import random

FIRST_NAMES = ['Bob', 'Alice', 'Frank', 'Ben', 'Niko', 'Vicky', 'Amanda']
LAST_NAMES = ['Harris', 'Barretto', 'Hansen', 'Smith']

def get_random_name():
    """
    Generates a random name.
    :return: Full random name as a string.
    """
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    return ' '.join([first_name, last_name])

if __name__ == '__main__':
    print(get_random_name())
