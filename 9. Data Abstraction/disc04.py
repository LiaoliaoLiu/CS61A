from doctest import run_docstring_examples


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:  # initial n should be postive
        return 1
    elif n < 0:
        return 0
    else:
        results = [count_k(n-i, k) for i in range(1, min(k, n)+1)]
        return sum(results)


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i*s[i] for i in range(0, len(s), 2)]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    def a_list_product(x):
        if x:
            return x[0] * a_list_product(x[1:])
        else:
            return 1

    if s:
        all_lists = []
        for i in range(2, len(s)):
            all_lists += [s[::i], s[1::i]]
        return max([a_list_product(x) for x in all_lists])
    else:
        return 1
