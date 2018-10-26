

def generate_fibonacci(n):

    """
    Generate the Fibonnaci sequence up to the n-th number.

    :param n: desired length of sequence (e.g. if n is 3, generate 0, 1, 1)
    """
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b
