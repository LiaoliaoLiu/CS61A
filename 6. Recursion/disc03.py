from doctest import run_docstring_examples


def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    assert n > 0, 'n must be a positive integer'
    print(n)
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return hailstone(n//2) + 1
        else:
            return hailstone(n*3+1) + 1


def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    '''
    if n1 == 0 and n2 == 0:
        return 0
    else:
        if n1 == 0:
            return 10*merge(n1, n2//10) + n2 % 10
        elif n2 == 0:
            return 10*merge(n1//10, n2) + n1 % 10
        elif n1 % 10 < n2 % 10:
            return 10*merge(n1//10, n2) + n1 % 10
        else:
            return 10*merge(n1, n2//10) + n2 % 10
    '''
    if n1 and n2:  # n1 = xxx, n2 = x
        if n1 % 10 < n2 % 10:
            return 10*merge(n1//10, n2) + n1 % 10
        else:
            return 10*merge(n1, n2//10) + n2 % 10
    else:  # n1 = xxx, n2 =0 or halting
        return max(n1, n2)


def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n-1))
    return repeat


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(n, k=2):
        if k == n:
            return True
        elif n % k == 0 or n == 1:
            return False
        else:
            return prime_helper(n, k+1)
    return prime_helper(n)
