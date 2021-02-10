from doctest import run_docstring_examples

def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False

def wears_jacket(temp, raining):
    return temp < 60 or raining

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    k = 2
    while n % k != 0:
        k += 1
    if k < n:
        return False
    else:
        return True

run_docstring_examples(is_prime, globals(), True)