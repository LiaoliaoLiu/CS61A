# Video
## Print and None
```
>>> print(None)
None # this is not a string
```
None is not displayed by the interpreter as the value of an expression
```
>>> a = print(None)
None
>>> a
>>> a=1
>>> a
1
```

## Miscellaneous about Python Features
### truedive, floordiv == /, //
### return multiple values in one return statement
### python3 -i \<some .py file>
> run python3 in interactive mode first execute \<>
### convention: using CAPs to refer former parameters

## Compound Statements
```
<header>:
    <statement>
    <statement>
    ...
<separating header>:
    <statement>
    <statement>
    ...
```
Statement - Clause - Suite(swit)
- A suite is a sequence of statements
- To "execute" a suite means to execute its sequence of statements, in order

Execution Rule for a sequence of statements:
- Execute the first statement
- Unless directed otherwise, execute the rest

```
def abs(x):
  if x < 0:
    return -x
  else:
    return x
```
1 statement, 2 clauses, 2 headers, 2 suites
>  A compound statement consists of one or more clauses

### conditional statements syntax tips
1. Always starts with "if" clause.
2. Zero or more "elif" clauses.
3. Zero or one "else" clasuse, always at the end.

## Boolean Contexts
### False values in Python:
False, 0, '', None (more to come)
### True values in Python:
Anything else (True)
```
>>> if -12:
...     print(7)
...
7
```

## Q&A
### Local frame rule
```
x = 2
def f():
    print(x)
    x = 3
    print(x)

>>> f()
UnboundLocalError: local variable 'x' referenced before assignment
-----
x = 2
def f(x):
    print(x)
    x = 3
    print(x)

>>> f(x)
2
3
```

# Ch. 1.3 Defining New Functions
## Environments
### Intrinsic and bound names
| Global |     |                |
| ------ | --- | -------------- |
| mul    | ->  | func mul(...)  |
| square | ->  | func square(x) |
- Intrisic name: the name appearing in the function
- Bound name: the name in a frame

### Function Signature
- Def: A description of the formal parameters of a function.
- Functions differ in the number of arguments that they are allowed to take.

### Local names
- Principle: The meaning of a function should be independent of the parameter names chosen by its author.
  - The simplest consequence: the parameter names of a function must remain local to the body of the function.
  - In other words: the *scope* of a local name is limited to the body of the user-defined function that defines it.
    - when a name is no longer accessibl, it is out of scope.

## Choosing names (style guide for Python code)
1. Function names are lowercase, separated by underscores, and descriptive.
2. Function names indicate operations (e.g., print, add, square) or results (e.g., max, abs, sum).
3. Parameter names are lowercase, separated by underscores. Single-word preferred.
4. Parameter names indicate role they took.
5. Avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals.

## Functions as Abstractions
3 aspects of a functional abstraction: (quares)
- The *domain* is any single real number
- The *range* is any non-negative real number.
- The *intent* is that the out put is the square of the input

# Ch. 1.4 Designing Functions
The qualities of good functions:
- Have exactly one job.
  - job should be identifiable with short text.
  - Multiple jobs, multiple functions
- Don't repeat youself. (DRY principle in software engineering)
  - logical should be implemented once, given a name, and applied multiple times.
  - Copying and pasting a block of code - consider functional abstraction
- General.
  - Squaring is not in Python Library because *pow* function

## Documentation
### Docstring
- indented along with the function body.
- Conventionally triple qouted.
- The first line describes the job of the function in one line.
- call *help(\<function_name>)* to see docstring
- Include docstrings for all but the simplest functions.
  - code is written only once, but often read many times.

### Comments 
Using # to comment

## Default Argument Values
In the *def* statement header, = does not perform assignment, but indicates a default value

# Ch. 1.5 Control
Executing a control statement determines what the interpreter should do next.

## Feature: *short-circuiting*
Truth value of a logical expression can sometimes be determined without evaluating all of its subexpressions.

    and
    or
    not

## Testing
### Assertions
Tests are typically written in the same file or a neighboring file with the suffix _test.py
```
>>> def fib_test():
        assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
        assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
        assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
```
### Doctest
Use
    
    run_docstring_examples(<function_name>, globals(), True) 

to test single function.
```
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

# Lab
Return with quotes: (qoutes stand for string)
```
>>> def test():
...     a = 'big'
...     return a
...
>>> test()
'big'
```

Boolean operators don't alwayls boolean (last evaluation)
```
>>> True and 13
13
>>> -1 and 1 > 0
True
>>> False or 0
0
>>> 1 and 3 and 6 and 10 and 15  
15
`