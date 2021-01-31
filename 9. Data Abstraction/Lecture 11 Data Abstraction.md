# Lecture
## Data abstraction
Compund objects combine objects together: a date(DD/MM/YY), a geographic position(latitude and longitude)

An abstract data type lets us manipulate compund objects as units, and isolate two parts of any program that uses data:
- How data are represented (as parts)
- How data are manipulated (as units)

Data abstraction: A methodology by which functions enforce an abstraction barrier between *representation* and *use*.

## Abstraction Barriers
## Data representation

## Dictionary
```python
>>> numerals = {'I': 1, 'V': 5, 'X': 10}
>>> numerals
{'I': 1, 'V': 5, 'X': 10}
>>> numerals['X']
10
>>> numerals[10] # can not do it reversely
KeyError: 10
>>> numerals.keys()
dict_keys(['I', 'V', 'X'])
>>> numerals.values()
dict_values([1, 5, 10])
>>> numerals.items()
dict_items([('I', 1), ('V', 5), ('X', 10)])
>>> items = [('I', 1), ('V', 5), ('X', 10)]
>>> items
[('I', 1), ('V', 5), ('X', 10)]
>>> dict(items) # transfer list to dict
{'I': 1, 'V': 5, 'X': 10}
>>> dict(items)['X']
10
>>> 'X' in numerals
True
>>> 'X-ray' in numerals
False
>>> {x:x*x for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> squares = {x:x*x for x in range(10)}
>>> squares[7]
49
>>> {1:2, 1:3} # keys are immutable
{1: 3}
>>> {1: [2,3]} # a key can have a *sequence* of multiple values
{1: [2, 3]}
>>> {[1]: 2} # a key can not be a list or dict
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

### Limitations on Dictionaires
Dictionaries are unordered collections of key-value pairs.

Dictionary keys do have two restrictions:
- A key of a dictionary cannot be a list or dictionary (or any mutable type) # Because of implementation of dictionaries in Python
- Two keys cannot be equal; One value for a given key. # Because it's part of the dictionary abstraction

## Q&A
### Abstraction Barriers
They are barriers to isolate different parts for large program, to manage complexity.

### How does the concept of a constructor and selector generalize to other examples beyond just rational numbers?
They are about data representation. Data abstraction gives you the tool to describle the attributes of a thing.

### Are data abstraction and object-oriented programming basically the same thing?
OOP are designed around data abstraction.

# Ch. 2.2
A function abstraction separates the way the function is used from the details of how the function is implemented. Analogously, data abstraction isolates how a compound data value is used from the details of how it is constructed.

Data abstraction should made programs use data in a way as to make as few assumptions about the data as possible. At the same time, a concrete data representation is defined as an independent apart of the program. These two parts of a program, one operates on abstract data, the other defines a concrete representation, are connected by a small set of functions that implement abstract data in terms of the concrete representation.

## The Properties of Data
```python
>>> def pair(x, y):
        """Return a function that represents a pair."""
        def get(index):
            if index == 0:
                return x
            elif index == 1:
                return y
        return get
>>> def select(p, i):
        """Return the element at index i of pair p."""
        return p(i)
```
With this implementation, we can create and manipulate pairs.
```python
>>> p = pair(20, 14)
>>> select(p, 0)
20
>>> select(p, 1)
14
```
Python doesn't actually work this way (lists are implemented more directly, for efficiency reasons) but that it could work this way. 

The functional representation, although obscure, is a perfectly adequate way to represent pairs, since it fulfills the only conditions that pairs need to fulfill. The practice of data abstraction allows us to switch among representations easily.

# Disc04
As a general rule of thumb, whenever you need to try multiple possibilities at the same time, you should consider using tree recursion.

Thus, lst[:] creates a list that is identical to lst (a copy of lst). lst[::-1] creates a list that has the same elements of lst, but reversed. Those rules still apply if more than just the step size is specified e.g. lst[3::-1].