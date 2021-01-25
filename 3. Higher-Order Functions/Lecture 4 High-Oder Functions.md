# Video
Higher-Order Functions: Functions manipulate other functions

## Designing functions
3 aspects: domain, range and intent
3 qualities: one job, DRY, general

## Higher-order functions
```
def cube(k):
    return pow(k,3)

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

>>> summation(5, cude)
225
```

### Locally Defined Functions
Functions defined within other function bodies are bound to names in a local fame
```
def make_adder(n)
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k)
        return k + n
    return adder
```

### The purpose of Higher-Order Functions
- Functions are first-class: Functions can be manipulated as values in Python.
- Higher-order function: A function that takes a function as an argument value or returns a function as a return value
  - Express general methods of computation
  - Remove repetition from programs
  - Separate concerns among functions

## Lambda expressions
```
>>> x = 10
>>> square = x * x
>>> x
10
>>> square
100
>>> square = lambda x: x * x
>>> square(10)
100
```
> lambda expresssions in Python cannot contain statements at all

### only def statement gives the function an intrinsic name
```
>>> square
<function <lambda> at xxxx>
>>> def square(x):
...     return x * x
...
>>> square
<function square at xxxx>
```

### Return statements & search
A return statement completes the evaluation of a call expression and provides its value
f(x) for user-defined function:
  - f: switch to a new environment;
  - execute f's body
  - return statement within f: switch back to the previous environment;
  - f(x) now has a value

```
def search(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)
```

## control
Why shortcut is necessary?

| Why Python use this | instead of this           |
| ------------------- | ------------------------- |
| If ____a:           | if_(____a, _____b, ____c) |
| ____b               |                           |
| else:               |                           |
| ____c               |                           |

Because: Call Expression Evaluation Rule. b will be evaluated even a is False.

### Logical operators
```
def reasonable(n):
    return n == 0 or 1/n != 0

>>> reasonable(0)
True
```

### Conditional Expressions
    <consequent> if <predicate> else <alternative>

# Ch. 1.6 Higher-Oder Functions
Without functions: Our programs would be able to compute squares, but our language would lack the ability to express the concept of squaring.

## 1.6.1 Functions as Arguments
See [Higher-order functions](##Higher-order-functions)

## 1.6.2 Functions as General Methods
- update: improve guess
- close: check guess
- improve: general expression of repetitive refinement

```
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess
```

## 1.6.3 Nested Definitions
### Lexical scope
Locally defined functions also have access to the name bindings in the scope in which they are defined (not where they are called). This discipline of sharing names among nested definitions is called lexical scoping.

To enable lexical scoping:
1. Each user-defined function has a parent environment: the environment in which it was defined.
2. When a user-defined function is called, its local frame extends its parent environment.

### Extended Environments
Python archieved lexical scoping by Extend Environments.

Two advantages of lexical scoping:
1. The names of a local function do not interfere with external names. - local function name bound in local environment.
2. A local function can access the environment of the enclosing function. - evaluation happend in extended environment.

> locally defined functions are often called closures.

## 1.6.4 Functions as Returned Values
function composition:
```
def compose1(f,g):
    def h(x):
        return f(g(x))
    return h
```

> convention: "1" in "compose1" signify that the function takes one argument.

## 1.6.5 Newton's Method
```
def find_zero(f, df):
    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update
    
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)
```
> near_zero's argument is guess

## Currying
Take multiple arguments into a chain of functions that each take a single argument.
```
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f(x, y)

>>> pow_curried = curry2(pow)
>>> pow_curried(2)(5)
32
>>> map_to_range(0, 10, pow_curried(2))
1
2
4
8
16
32
64
128
256
512
```
    curry2 = lambda f: lambda x: lambda y: f(x, y)
> currying is bit like cordinate mapping (3D)

> the secret when you use "f" without parenthesis, you don't call it.

## Lambda Expresssions
Unnamed functions
```
compose1 = lambda f,g: lambda x: f(g(x))
```
| lambda          | x       | :           | f(g(x)) |
| --------------- | ------- | ----------- | ------- |
| A function that | takes x | and returns | f(g(x)) |

## Abstractions and First-Class Functions
Be aware to opportunities to indentify the abstractions in programs, build upon them, and generalize them to create more powerful abstractions.

Choose the level of abstraction appropriate to their task.

Elements with the fewest restrictions are said to have first-class status:
   1. They may be bound to names.
   2. They may be passed as arguments to functions.
   3. They may be returned as the results of functions.
   4. They may be included in data structures.

Python awards functions full first-class status.

## Function Decorators
```
def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
            return fn(x)
        return wrapped
        
@trace
def triple(x):
    return 3 * x

>>> triple(12)
->  <function triple at 0x102a39848> ( 12 )
36
```
This decorator is equivalent to:
```
def triple(x):
    return 3 * x

triple = trace(triple)
```
You can't use lambda expression after @:
```
@lambda f: lambda x: f(x)+1
def f(x):
    return 2*x

b = f(1)
SyntaxError: invalid syntax (<string>, line 1)
```

# Disc01

Assignmenets for def statements use pointers to funcions, which can have different behavior than primitive assignments.

# Hog
Commentary part and make_averaged did a currying. -> why we need currying?