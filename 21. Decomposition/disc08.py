"1.1"
class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2

class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret

"""
>>> b = B()
>>> b.add_a(A("a"))
>>> b.add_a(A("b"))
>>> b
2
aabb
"""

"2.1"
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    sum, t = 0, lnk
    while t != Link.empty:
        sum += t.first
        t = t.rest

    return sum

""" 2.2
Write a function that takes in a Python list of linked lists and multiplies them
element-wise. It should return a new linked list.
If not all of the Link objects are of equal length, return a linked list whose length is
that of the shortest linked list given. You may assume the Link objects are shallow
linked lists, and that lst of lnks contains at least one linked list.
"""
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    product = 1
    for s in lst_of_lnks:
        if s == Link.empty:
            return Link.empty
        product *= s.first
    lst_of_rest_lnks = [s.rest for s in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_rest_lnks))
""" 2.3
Write a recursive function flip two that takes as input a linked list lnk
and mutates lnk so that every pair is 
ipped.
"""
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    t = lnk
    while t.rest != Link.empty and t.rest.rest != Link.empty:
        t.rest.first, t.first = t.first, t.rest.first
        t = t.rest.rest

"2.3"
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link == link.empty:
        yield StopIteration
    elif f(link.first):
        yield link.first
    else:
        yield filter_link(link.rest, f)
        
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
