# Lecture
## Objects
- Objects represent information
- They consist of data and behavior, bundled together to creat abstractions
- Objects can represent things, but aslo properties, interactions, & processes
- A type of object is called a class; classes are first-class values in Python
- Object-oriented programming:
  - A metaphor for organizing large programs
  - Special syntax that can improve the composition of programs
- In python, every values is an object
  - All objects have attributes
  - A lot of data manipulation happens through object methods
  - Functions do one thing;45 bjects do many ralated things.

## Mutation
There is a change in object.

- The same object can change in value throughout the course of computation
- All names that refer to the same object are affected by a mutation
- Only objects of *mutable* types can change: lists & dictionaries

## Tuples
- Immutable sequence.
- They can be used as key in dictionary. (lists can't)
- An immutable sequence may still change if it contains a mutable value as an element

```python
>>> s = ([1, 2], 3)
>>> s[0][0] = 4
>>> s
([4, 2], 3)
>>> s[0] = 4
ERROR
```

## Identity Operators
### Identity
```python
<exp0> is <exp1>
```
evaluates to True if both \<exp0> and \<exp1> evaluate to the same object
### Equality
```python
<exp0> == <exp1>
```
... evaluate to the same values

Indentical obejcts are always equal values.

## Mutable Default Arguments are Dangerous
```python
>>> def f(s=[]): # maybe you can use it to track the function was called. But you should avoid it.
...     s.append(5)
...     return len(s)
>>> f()
1
>>> f()
2
>>> f()
3
```

## List in Environment Diagrams
Assume: s = [2, 3] t = [5, 6]

<table>

<tr>
<td> Opeartion </td> <td> Example </td> <td> Result</td>
</tr>

<tr>
<td> 
*append* adds one<br>
element to a list
</td>
<td> 
s.append(t)<br>
t = 0
</td>
<td>
s -> [2, 3, [5, 6]]<br>
t -> 0
</td>
</tr>

<tr>
<td> 
*extend* adds all elemetns<br>
in one list to another list
</td>
<td>
s.extend(t)<br>
t[1] = 0
</td>
<td>
s -> [2, 3, 5, 6]<br>
t -> [5, 0]
</td>
</tr>

<tr>
<td> 
*addition* & *slicing* creat new lists <br>
containing existing elements<br>
</td>
<td>
a = s + [t]<br>
b = a[1:]<br>
a[1] = 9<br>
b[1][1] = 0
</td>
<td>
s -> [2, 3]<br>
t -> [5, 0]<br>
a -> [2, 9, [5, 0]]<br>
b -> [3, [5,0]]
</td>
</tr>

<tr>
<td> 
The *list* function also <br>
creats a new list <br>
containing existing elements
</td>
<td>
t = list(s)<br>
s[1] = 0
</td>
<td>
s -> [2, 0]<br>
t -> [2, 3]
</td>
</tr>

<tr>
<td>
*slice assignment* replaces<br>
a slice with new values<br>
or [] (remove)
</td>
<td>
s[0:0] = t<br>
s[3:] = t<br>
t[1] = 0
</td>
<td>
s -> [5, 6, 2, 5, 6]<br>
t -> [5, 0]
</tr>

<tr>
<td>
*remove* removes the first element<br>
equal to the argument
</td>
<td>
t.extend(t)<br>
t.remove(5)
</td>
<td>
s -> [2, 3]<br>
t -> [6, 5, 6]
</td>
</tr>

</table>

```python
>>> t = [1, 2, 3]
>>> t[1:3] = [t]
>>> t.extend(t)
[1, [...], 1, [...]]

>>> t = [[1, 2], [3, 4]]
>>> t[0].append(t[1:2])
[[1, 2, [[3, 4]]], [3, 4]]
```

# Q&A
## Slice Assignment
```python
>>> s = [1,2,3]
>>> t = [4,5,6]
>>> s[0:0] = t # s must be a list like object. t must be an iterable *container*
>>> s
[4,5,6,1,2,3] # behold "1"

>>> s = [1,2,3]
>>> t = [4,5,6]
>>> s[0:1] = t 
>>> s
[4,5,6,2,3] # no "1" here, that's the how it work

>>> s = [1,2,3]
>>> t = [4,[5],6]
>>> s[1:2] = t 
>>> s
[1,4,[5],6,3] # notice the [5], it's an object pointer
>>> t[1][0] = 4
>>> s
[1, 4, [4], 6, 3]]

>>> s = [1,2,3]
>>> s[1:2] =[]
>>> s
[1,3]
```

# Ch. 2.4
## Tuples
Parentheses are optional but used commonly in practice.
```python
>>> 1, 2 + 3
(1, 5)
```

*count* and *index* work here as list
```python
>>> code = ("up", "up", "down", "down") + ("left", "right") * 2
>>> len(code)
8
>>> code[3]
'down'
>>> code.count("down")
2
>>> code.index("left")
4
```

Tuples are used implicitly in multiple assignment, An assignment of two values to two names creates a two-element tuple and then unpacks it.

## Dictionaries
Values stored and retrieved are indexed not by consecutive integers, but by descriptive keys.

- The methods keys, values, and items all return iterable values.
```python
>>> sum(numerals.values())
66
```
- A list of key-vaule, pairs can be converted into a dictionary by constructor.
```python
>>> dict([(3, 9), (4, 16), (5, 25)]) # you can replace (3, 9) ... with [3, 9]
{3: 9, 4: 16, 5: 25}
```
- Two restrictions
  - A key of a dictionary cannot be or contain a mutable value.
  - There can be at most one value for a given key. But the value can be a sequence.
- The metho *get* returns value for a key or a default value.
```python
>>> numerals.get('A', 0)
0
>>> numerals.get('V', 0)
5
```

## Local State
```python
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount # The binding is changed in make_withdraw's frame, not withdraw's
        return balance
    return withdraw
```
- Recall *balance* without the nonlocal statement, an assignment statement would always bind a name in the first frame of the current (Here is withdraw's frame). 
- After executing nonlocal *balance*, **any assignment** statement with *balance* on the left-hand side of = will not bind balance in the first frame of the current environment. 
- Instead, it will find the first frame in which balance was already defined and re-bind the name in that frame. 
- If balance has not previously been bound to a value, then the nonlocal statement will give an error.
- No nonlocal statement is required to **access** a non-local name. By contrast, only after a nonlocal statement can a function **change** the binding of names in these frames.

### Python Particulars
- Non-local assignment is often the default behavior of assignment statements in other programming language. 
- This cause an unusual restriction that all instances of a name must refer to the same frame in Python. 
- As a result, Python cannot look up the value of a name in a non-local frame, then bind that same name in the local frame.
- This restriction allows Python to **pre-compute** which frame contains each name before executing the body of a function. 

```python
def make_withdraw(balance):
    def withdraw(amount):
        if amount > balance: # This will err because balance is also assigned in line 5
            return 'Insufficient funds'
        balance = balance - amount 
        return balance
    return withdraw
```