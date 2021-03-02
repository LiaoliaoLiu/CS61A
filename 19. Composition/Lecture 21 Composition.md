# Lecture
## Linked List
### Linked List Structure
A linked list is either empty *or* a first value and the rest of the linked list.

    Link(3, Link(4, Link(5, Link.empty)))

- A linked list is a pair
- A class attribute represents an *empty* linked list
- The first (zeroth) element is an attribute value
- The rest ofthe elements are stored in a linked list

### Linked List Class
Attributes are passed to \__init__
```python
class Link:
    empty = ()      # Do what you think right, other zero-length sequences are fine

    def __init__ (self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link) # Work well in inheritance
        self.first = first
        self.rest = rest
```
> Linked list usually is immutable

## Linked List Processing
## Linked List Mutation
Attribute assignment statements can change first and rest attributes of a Link.
```python
# The rest of a linked list can contain the linked list as a sub-list
>>> s = Link(1, Link(2, Link(3)))
>>> s.first = 5
>>> t = s.rest
>>> t.rest = s
>>> s.first
5
>>> s.rest.rest.rest.rest.rest.first
2 # odd rest's first = 2, even rest's first = 5

"""bad taste"""
def add(s, v):
    prev = Link.empty
    curr = s
    while curr != Link.empty:
        if v < curr.first and prev.first != v:
            prev.rest = Link(v, curr)
        prev = curr
        curr = curr.rest
    if prev.first < v
        prev.rest = Link(v, curr)
"""John's taste"""
def add_john(s, v):
    assert s is not List.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add_john(s.rest, v)
    return s
```

## Tree Class
## Tree Mutation
## Q&A
- 00:03​ Are linked lists used a lot, or do most people just use lists?
  - It doesn't show up that often. One advantage it taht Linked lists can insert element without moving around whole list in memory.
- 02:48​ HW4 Q4: Permutations
  - for i in range(len(s)). copy the list, pop the element, put the poped list into recursion.
- 08:04​ Are nested for loops necessary for permutations?
- 09:13​ Can permutations be solved by insertion? What can go wrong?
- 16:38​ Is a circular linked list ever a good idea?
  - suited for certain situation like what's the 50th digit of one divided by seven (call rest 50 times)
- 20:05​ Discussion 5 Q 1.3 square_tree
- 24:40​ Spring 2019 MT2 Q1
- 33:54​ Spring 2015 MT2 Q4(b)
  - fisrt, rest = s[:k], s[k:]

# Ch. 2.9
## Recursive Object
When an object of some class has an attribute value of that same class, it is a recursive object.

## Linked List Class
- len() calls \__len()__
- selection operator [] calls \__getitem__
```python
class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    def __len__(self):
        return 1 + len(self.rest)

>>> s = Link(3, Link(4, Link(5)))
>>> len(s)
3
>>> s[1]
4
```

For readability and debugging, a string repr can help:
```python
def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' + link_expression(s.rest)
    return 'Link({0}{1})'.format(s.first, rest)
>>> link_expression(s)
'Link(3, Link(4, Link(5)))'
>>> Link.__repr__ = link_expression
>>> s
Link(3, Link(4, Link(5)))
```

Like Tree, this Link class has the closure property. A Link can contain a Link as its *first* element:
```python
>>> s_first = Link(s, Link(6))
>>> s_first
Link(Link(3, Link(4, Link(5))), Link(6))
```

How about implement "+"?
```python
def extend_link(s, t):
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))
>>> extend_link(s, s)
Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
>>> Link.__add__ = extend_link
>>> s + s
Link(3, Link(4, Link(5, Link(3, Link(4, Link(5))))))
```

map and filter are not much different from Iterators.

## Sets
- menbership tests
- length computation
- standard set operations like union and intersection.

### Sets as Unordered Sequences
```python
def empty(s):
    return s is Link.empty
def set_contains(s, v):                                     # O(n)
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)
def adjoin_set(s, v):                                       # O(n)
    """Return a set containing all elements of s and element v."""
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)
def intersect_set(set1, set2):                              # O(n^2)
    """Return a set containing all elements common to set1 and set2."""
    return keep_if_link(set1, lambda v: set_contains(set2, v))
def union_set(set1, set2):                                  # O(n^2)
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = keep_if_link(set1, lambda v: not set_contains(set2, v))
    return extend_link(set1_not_set2, set2)
```

### Sets as Ordered Sequences
```python
def set_contains(s, v):
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)

def intersect_set(set1, set2):              # O(n) len(set1) + len(set2)
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect_set(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect_set(set1.rest, set2)
        elif e2 < e1:
            return intersect_set(set1, set2.rest)
```

### Sets as Binary Search Trees
```python
def set_contains(s, v):                 # O(logn) if tree is balanced
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains(s.right, v)
    elif s.entry > v:
        return set_contains(s.left, v)

def adjoin_set(s, v):
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Tree(s.entry, s.left, adjoin_set(s.right, v))
    elif s.entry > v:
        return Tree(s.entry, adjoin_set(s.left, v), s.right)
```
ince the position of a newly adjoined element depends on how the element compares with the items already in the set, we can expect that if we add elements "randomly" the tree will tend to be balanced on the average.

One way to solve this problem is to define an operation that transforms an arbitrary tree into a balanced tree with the same elements. We can perform this transformation after every few adjoin_set operations to keep our set in balance.

Intersection and union operations can be performed on tree-structured sets in linear time by converting them to ordered lists and back.

### Python set Implementation
Python uses a representation that gives constant-time membership tests and adjoin operations based on a technique called *hashing*. Built-in Python sets cannot contain mutable data types, such as lists, dictionaries, or other sets. To allow for nested sets, Python also includes a built-in immutable *frozenset* class that shares methods with the set class but excludes mutation methods and operators.