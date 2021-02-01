# Lecture
## The Closure Property of Data Types
The result of combination can itself be combined using the same method. (Lists can contain lists)
- Closure is powerful because it permits us to creat hierarchical structures
- Hierarchical structures are made up of parts, which themselves are made up of parts, and so on

### Box-and-Pointer notation
Lists are represented as a row of index-labeled adjacent boxes, one per element. Each box either contains a primitive value or points to a compound value.
```python
pair = [1, 2]
nested_list = [[1, 2], [], [3, False, None], [4, lambda: 5]]
```

## Processing Container Values
```python
>>> [x < 5 for x in range(5)]
[True, True, True, True, True]
>>> all([x < 5 for x in range(5)])
True
>>> all(range(5)
False
```

## Tree Abstraction
Recursive description (**wooden tree**):
- A **tree** has a root **label** and a list of **branches**.
- Each **branch** is a **tree**
- A tree with zero branches is called a **leaf***

Relative description (**family trees**):
- Each location in a tree is called a **node**
- Each **node** has a **label** that can be any value
- One node can be the **parent/child** of another

People often refer to labels by their locations: "each parent is the sum of its children"

### Implementing the Tree Abstraction
```python
def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches) # here is the trick, branches must be a *list of tree* not *tree*.

def label(tree):
    return tree[0]

def branches(tree):
    """Branches always returns alist.

    If that list is not empty, every element is a tree. (could be empty)
    """
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

>>> tree(3, [tree(1),
...          tree(2, [tree(1),
...                   tree(1)])])
[3, [1], [2, [1], [1]]]

>>> tree(1, [5])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in tree
AssertionError: branches must be trees
>>> tree(1, [[5]])
[1, [5]]
>>> tree(1 ,[tree(5)])
[1, [5]]

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

def count_leaf(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaf(b) for b in branches(b)])

>>> sum([ [1] ], [])
[1]
>>> sum([ [[1]],[2] ], [])
[[1], 2]

def leaves(tree):
    """return a list containing the leaf labels of trees.
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    if is_leaf(t):
        return tree(label(t) + 1) # check the return value type *immediately*
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])

def increment(t):
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  '*indent + str(label(t)))
    for b in branches(t):
        print(b, indent+1)
```

## Example: Summing Paths
Two ways to build up result:
- manipulating the return value
- passing information into the result as an argument (tail recursion)
```python
def fact_times(n, k):
    "return k * n * (n-1) * ... * 1"
    if n == 0:
        return k
    else:
        return fact_times(n-1, k * n)

def fact(n):
    return fact_times(n, 1)

numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'),
                              tree('t')]),
                   tree('e')])

def print_sums(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)

>>> print_sums(numbers, 0)
7
14
>>> print_sums(haste, '')
has
hat
he
```

## Q&A
When you call label on sth, you should always call with sth created by calling tree, same as branches. This is a rule about data abstraction in general. Selectors should always only take results that from calling a constructors.

# Ch. 2.3
## Partition trees
- the left (index 0) branch contains all ways of partitioning n using at least one m,
- the right branch contains partitions using parts up to m-1,
- the root label is m

```python
def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(parition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)
```

## Binarization
```python
def right_binarize(tree):
    if is_leaf(tree):
        return tree
    if len(tree) > 2
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree] # there may be a tree in right that is not a binary tree.
```