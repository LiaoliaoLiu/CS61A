# Lecture
```py
def merge(s, t):
    """Return a sorted Link with elements of sorted s & t. With auxiliary space"""
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))

def merge_in_place(s, t):
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t
```

## Q & A
- 00:09​ Spring 2017 Mock Midterm 2 Question 4
```
1   2   3   4   5   6   7   8
1   3       7   12      19  27  # skip 3rd
1           8           27      # skip 2nd
```
- 08:34​ Summer 2020 Practice Midterm Question 3
```py
def every_subseq(n):
    """Yield every number "within" n."""
    if n == 0:
        yield n
    else:
        for rest in every_subseq( n // 10):
            yield rest
            yield 10 * rest + n % 10

# 1) Forget about n % 10 and just find close(n // 10)
# OR
# 2) Use          n % 10 and make sure that everything before it forms a "near increasing" sequence
def close(n, smallest=10, d=10, current_len=0):
    """ return the longest near increasing subsuq of n (int)
    near increasing: each element but the last two is smaller than all elements in the sequence.
    >>> close(1523)
    153
    >>> close(15123)
    1123
    >>> close(111111111)
    11
    >>> close(45671)
    4567
    >>> close(1325)
    135
    >>> close(325)
    35
    >>> close(13245768)
    134578
    """
    if n == 0:
        return 0
    no = close(n//10, smallest, d, current_len)
    if smallest > n % 10 and (d >= n % 10 or current_len < 2):
        yes = close(n//10, min(smallest, d), n%10, current_len + 1) * 10 + n % 10
        return max(no, yes)
    return no
```
- 22:45​ Can you mix return and yield?
  - Yes, but this is werid.
- 23:30​ Summer 2020 Practice Midterm Question 3 (revisited)
- 28:43​ Does order matter in a multiple assignment statement with attributes?
  - L.rest, L = L.rest.rest, L.rest.rest
- 30:45​ When an instance attribute and class attribute have the same name but they are functions, which one do you look up?
  - Instance first.

## Lecture 25 Q&A
02:55​ Lab 9 Q4: Number of full binary trees
- 13:21​ Spring 2020 Midterm 2 Question 1
- 24:50​ Fall 2018 Midterm 1 Question 7
```py
def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.

    >>> [f(v) for f in lookups(k, 2)]
    ['C', 'A']
    >>> [f(v) for f in lookups(k, 2)]
    ['S']
    >>> [f(v) for f in lookups(k, 2)]
    []
    """
    if k.label == key:
        yield lambda v: v.label
    for i in range(len(k.branches)):
        for lookup in lookups(k.branches[i], key):
            yield new_lookup(i, lookup)                     # lookup is not lookups
    
def new_lookup(i, f):
    def g(v):
        return f(v.branches[i])
    return g
```