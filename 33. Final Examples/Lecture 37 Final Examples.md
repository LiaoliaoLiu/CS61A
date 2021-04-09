# Lecture
## Trees
One important reason to learn about recursion is in order to manipulate tree structure data.

### Tree Processing
Implement *bigs*, which takes a Tree instance t containing integer labels. It returns the number of nodes in t whose labels are larger than all labels of their ancestor nodes.

1. understand the problem.
   - 'It returns the number of nodes in t whose labels are larger than all labels of their ancestor nodes.'
2. walk through an example before ever trying to write code
   - A diagram is always helpful
3. think about what I expect to appear somewhere within the implementation
```py
if t.is_leaf():
    return ___
else:
    return ___([___ for b in t.branches])
```
   - this structure doesn't track 'ancestor', so think something else.
   - think about an option that doesn't work out is fine, as long as you figure this out quickly
   - ask youself what this needs
```py
if node.label > max(ancestors): # or
if node.label > max_ancestors:  # got it!

def bigs(t):
    def f(a, x):
        if a.label > x:
            return 1 + sum([f(b, a.label) for b in b.branches])
        else:
            return sum([f(b, x) for b in b.branches])

    return f(t, a.label-1)
```
4. label what a variable means if neccessary
5. check your work
   - figuring why a function doesn't work almost always involves you manually tracing through

### Recursive Accumulation
There are rarely a huge number of different ways to archieve a goal, instead, there are often a few common patterns that get applied over and over again.

1. return the accumulation (what we just saw)
2. initialize some accumulation

They are differernt in a limited sense.
```py
def bigs(t):
    n = 0
    def f(a, x):
        nonlocal n
        if a.label > x:
            n += 1
        for b in a.branches:
            f(b, max(a.label, x))

    return f(t, a.label-1)
```

## Designing Functions
> It is *eamples driven*

1. From Problem Analysis to Data Definitions
   - Identify the information that must be represented and *how* it is represented in the chosen programming language. 
   - Formulate data definitions and illustrate them with examples.

2. Signature, Purpose Statement, Header (domain and range)
   - State what kind of data the desired function consumes and produces. 
   - Formulate a concise answer to the question *what* the function computes. 
   - Define a stub that lives up to the sugnature

3. Function Examples
   - Work through examples that illustrate the function's purpose.

4. Function Template (control statements, function calls should be made in the body)
   - Translate the data definitions into an outline of the function.

5. Testing

   - Articulate the examples as tests and ensure that the function passes all. 
   - Doing so discovers mistakes. Tests also supplement examples in that they help others read and understand the definition when the need arises--
   - and it will arise for any serious program.

This is not a perfect way to design a function, but it's a useful way when you have problem writing a function.

### Applying the Design Process
Implement smalls, which takes a Tree instance t containing integer labels. It returns the non-leaf nodes in t whose labels are smaller than any labels of their descendant nodes. 

```py
def smalls(t):  # one has already been done.
    """Return the non-leaf nodes in t that are smaller than all their descendants.
    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """
    result = [] # Signature: Tree -> List of Trees
    def process(t):
    # Signature: Tree -> number
    # " Find smallest label in t & maybe add t to the result
        if t.is_leaf():
            return t.label
        else:
            smallest = min([process(b) for b in t.branches])
            if t.label < smallest
                result.append(t)
            return min(smallest, t.label)
    process(t)
    return result
```

## Q&A
- 00:07​ Spring 2018 Final Questin 5(a)
```py
def scurry(f, n):
    def h(k, args_so_far):
        if k == 0:
            return f(args_so_far)
        return lambda x: h(k-1, args_so_far + [x])
    return h(n, [])
```
- 06:17​ Spring 2018 Final Questin 5(b)
```py
def factorize(n, k=2):
    if n==k:
        return 1
    elif k > n:
        return 0
    elif n % k != 0:
        return factorize(n, k+1)
    return factorize(n, k+1) + factorize(n // k, k)
```
- 15:26​ How do you refer to a particular argument in a function/procedure that takes a variable number of arguments?
  - *(args) **(kargs)
- 17:13​ Spring 2020 Final Question 4(a)
- 22:32​ Fall 2019 Final Question 1