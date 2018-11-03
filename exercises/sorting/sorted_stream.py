def sorted_stream(*streams):
    """
    Given a list of streams sorted in ascending order, combine their outputs and produce one fully sorted stream.
     Example:
        given streams are 2 streams producing (1, 3, 5) and (2, 4, 6) respectively,
        the generator returned should produce (1, 2, 3, 4, 5, 6).

    :param streams: Sorted iterators
    :return: A generator which yields the sorted elements of all streams.
    """
    pass