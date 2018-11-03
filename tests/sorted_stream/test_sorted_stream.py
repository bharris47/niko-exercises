import unittest
from itertools import count, islice

from exercises.sorting.sorted_stream import sorted_stream


class SortedStreamTests(unittest.TestCase):
    def test_sorted_stream_quick(self):
        streams = [
            (i for i in range(1, 7, 2)),
            (i for i in range(2, 8, 2))
        ]
        stream = sorted_stream(*streams)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(list(stream), expected)

    def test_sorted_stream_more_streams(self):
        streams = [
            (i for i in range(1, 7, 2)),
            (i for i in range(2, 8, 2)),
            (i for i in range(5, 10, 2)),
            (i for i in range(8, 15, 2)),
            (i for i in range(2, 10, 3)),
        ]
        stream = sorted_stream(*streams)
        expected = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 12, 14]
        self.assertListEqual(list(stream), expected)

    def test_sorted_stream_endless(self):
        streams = [
            count(1, 2),
            count(2, 4),
            count(3, 10),
            count(2, 3),
            count(5, 5),
            count(6, 7),
        ]
        stream = sorted_stream(*streams)
        value = next(islice(stream, 1000000, 1000001))
        expected = 655227
        return self.assertEqual(value, expected)