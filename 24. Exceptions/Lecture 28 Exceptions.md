# Lecture
## Handling Errors
Grace Hopper's Notebook, 1947, Moth found in a Mark II Computer (Bug)

## Exceptions
- A built-in mechanism in a programming language to declare and respond to exceptional conditions
- Python *raises* an exception whenever an error occurs.
- Exceptions can be *handled* by the program, preventing the interpreter from halting.
- Unhandled exceptions will cause Python to halt execution and print a *stack trace*.

**Mastering exceptions:**
- Exceptions are objects! They have classes with constructors.
- They enable non-local continuations of control:
  - If *f* calls *g* calls *h*, exceptions can shift control from *h* to *f* without waiting for *g* to return.
- (Exception handling tends to be slow.) They are for non-standard situations.

## Assert Statements
```py
assert <expression>, <string>
```
Assertions are designed to be used liberally. They can be ignored to increase efficiency by running Python with the "-O" flag. "O" stands for optimized.
```py
python3 -O  # Whether assertions are enabled is governed by a bool __debug__
>>> __debug__
False
```

## Raise Statements
Exception are raised with a raise statement.
```py
raise <expression>
```
- \<expression> must evaluate to a subclass of BaseException of an instance of one.
- Exceptions are constructed like any other object. E.g., TypeError('Bad argument!')
  - *TypeError* -- A function was passed the wrong number/type of argument
  - *NameError* -- A name wasn't found
  - *KeyError* -- A key wasn't found in a dictionary
  - *RuntimeError* -- Catch-all for troubles during interpretation
```py
>>> raise TypeError('Bad argument')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Bad argument

>>> abs('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
```

## Try Statements
Try statements handle exceptions
```py
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
```
**Execution rule:**
- The \<try suite> is executed first.
- If, while executing the \<try suite>, an exception is raised that is *not handled*, and
- If the class of the exception inherits from \<exception class>, then
- The \<except suite> is executed, with \<name> bound to the exception.

## Handling Exceptions
**Multiple try statements:** Control jumps to the except suite of the most recent try statement that handles that type of exception.
```py
def invert(x):
    result = 1/x
    return result

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

>>> try:
...     invert_safe(0)
... except ZeroDivisionError as e:
...     print('Handled!')
...
'division by zero'
```

## Reducing a Sequence to a Value
```py
def reduce(f, s, initial):
    """
    >>> reduce(mul, [2, 4 ,8], 1)
    64
    """
```
- *f* is a two-argument function
- *s* is a sequence of values that can be the second arguement
- *initial* is a value taht can be the first argument
- the return value should be able to pass to f
```py
def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
# Implememtation of reduce doesn't need to know anything about ZeroDivisionError
# We use another function to handle the error
```

## Q&A
- 01:33​ Why is exception handling slow?
  - Raise exception will make interpreter go a irregular order, which is called bookkeeping takes a lot of instructions, reducing the efficiency. But "slow" is relative, in microsecond level.
- 04:19​ What is a finally clause in a try statement?
```py
try:
    ... # this line always gets executed
    ... # Raise exception
    ... # If this one is what you put in finally, it will not run
except ...:
    ...
finally:
    ... # this will always run. often releasing resources.
```
- 07:06​ What does the header name get bound to in an except clause?
```py
def return_an_error():
    try:
        1/0
    except ZeroDivisionError as n:
        print("n is", n)
        return n

>>> e = return_an_error()
n is division by zero
>>> e
ZeroDivisionError('division by zero')
>>> str(e)
'division by zero'
>>> repr(e)
"ZeroDivisionError('division by zero')"
# You want the "e" to track exceptions
```
- 09:38​ Fall 2019 Final Question 7
- 20:23​ What does the map procedure do?
- 21:21​ What's the difference between cons, list, and append?
  - cons is the most fundamental operation. list save your time to type cons.
```scheme
scm> (append (list 1 2) (list 3 4 5))
(1 2 3 4 5)
```

# Ch. 3.3
## Raising exceptions
In addition, the interpreter will print a *stack backtrace*, which is a structured block of text that describes the nested set of active function calls in the branch of execution in which the exception was raised.

## Example: Exception Objects
```py
# First, we define a new Exception subclass
class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess
# Next, we define a version of improve with exceptions handling
def improve(update, done, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)   # Behold!
# Finally, we define find_zero
def find_zero(f, guess=1):
    def done(x):
        return f(x) == 0
    try:
        return improve(newton_update(f), done, guess)
    except IterImproveError as e:
        return e.last_guess

>>> from math import sqrt
>>> find_zero(lambda x: 2*x*x + sqrt(x))
-0.030211203830201594
```
Although this approximation is still far from the correct answer of 0, some applications would prefer this coarse approximation to a *ValueError*.

Exceptions are another technique that help us as programs to separate the concerns of our program into modular parts. In this example, Python's exception mechanism allowed us to separate the logic for iterative improvement, which appears unchanged in the suite of the *try* clause, from the logic for handling errors, which appears in *except* clauses.