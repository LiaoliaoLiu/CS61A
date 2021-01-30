# Lecture
## List
Think index as offset from the beginning.

```python
>>> a = [1, 2, 3, 4]
>>> a[1:] # slicing, equals to a[1:len(a)], [), creates a new list
[2, 3, 4]
>>> a[3:]
[5]
>>> a[3:] == 4
False
>>> a[3] == 4
True
>>> a[-1]
4
>>> a[-2]
3
>>> a[1:-1] # equals to a[1:len(t)-1]
[2, 3]
>>> a[-1:1:-1]
[4, 3]
```
> range is not a list (to make it compact)

### List Comprehensions
```python
>>> letters = ['a', 'b', ... 'z']
>>> [letters[i] for i in [3, 4, 6, 8]]
['d', 'e', 'm', 'o']

>>> letters[i] for i in range(3)
  File "<stdin>", line 1
    letters[i] for i in range(3)
               ^
SyntaxError: invalid syntax)

def divisors(n):
    return [1] + [x for x in range(2,n) if n%x==0]
```

### Concatenation and Repetition
```python
>>> digits = [1, 8, 2, 8]
>>> [2, 7] + digits * 2
[2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
```

## Containers
```python
>>> [1, 2] in [3, [[1, 2]], 4]
False
```
It doesn't search deeply. It just search an element by an element.

## For Statement
```python
def count(s, value):
    """
    >>> count([1, 2, 1, 2, 1], 1)
    3
    """
    total = 0
    for element in s: # This should explain how for _ in _ works
        if element == value:
            total += 1
    return total

for <name> in <expression>:
    <suite>
```
execution procedure:
1. Evaluate the header \<expression>, which must yield an *iterable* value (a sequence)
2. For each element in taht sequence, in order:
   1. Bind \<name> to that element in the current frame
   2. Execute the \<suite>

### Sequence Unpacking in For Statements
```python
>>> pairs = [[1, 2], [2, 2], [3, 2], [4, 4]] # A sequence of fixed-length sequence
>>> same_count = 0
>>> for x, y in paris: # x, y are names for each element in a fixed-length sequence
...         if x == y:
...             same_count += 1

>>> same_count
2
```

## String
### Strings are an Abstraction
```python
>>> exec('curry = lambda f: lambda x: lambda y: f(x, y)')
>>> curry
<function <lambda> at 0x7feec96de790>
```

### Three forms
```python
>>> 'I am string'
'I am string'

>>> "I've got an apostrophe"
"I've got an apostrophe"

>>> """The Zen of Python
... claims, Readability counts."""
'The Zen of Python\nclaims, Readability counts.'

>>> 'I've got an apostrophe'
  File "<stdin>", line 1
    'I've got an apostrophe'
       ^
SyntaxError: invalid syntax
```

### Strings are Sequences
```python
>>> city = 'Berkeley'
>>> len(city)
8
>>> city[3]
'k' # It's stil a string with one character. But a list will return a number not a list
```
When working with strings, we usually care about whole words more than letters:
```python
>>> 'here' in "where's Waldo?"
True
>>> 234 in [1, 2, 3, 4]
False
>>> [2, 3, 4] in [1, 2, 3, 4, 5]
False
```

### Reverse a string
```python
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
```

# Ch. 2.1
## Native data types 
properties:
1. There are expressions that evaluate to values of native types, called *literals*
2. There are built-in functions and operators to manipulate values of native types.

## Differences betweem int and float
int objects are exact, while float objects are approximations to real values.

# Ch. 2.3
A sequence is an ordered collection of values. They are not not instances of a particular built-in type or abstract data representation, but instead a collection of behaviors that are shared among several different types of data.
- Length. A sequence has a finite length. An empty sequence has length 0.
- Element selection. A sequence has an element corresponding to any non-negative integer index less than its length, starting at 0 for the first element.

## Sequence unpacking
The pattern of binding multiple names to multiple values in a fixed-length sequence is called [*sequence unpacking*.](###sequence-unpacking-in-for-statements) 

## List Comprehension
The *for* keyword is not part of a *for* statement, but instead part of a list comprehension because it is contained within square brackets.

The general form of a list comprehension:
    
    [<map expression> for <name> in <sequence expression> if <filter expression>]

