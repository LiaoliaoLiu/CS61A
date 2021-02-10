def GCD(a, b):
    """
    >>> GCD(10, 5)
    5
    >>> GCD(27, 13)
    1
    """
    for i in range(min(a, b), 0, -1):
            if a % i == b % i == 0:
                return i