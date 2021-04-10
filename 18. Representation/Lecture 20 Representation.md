# Lecture
## String Representations
> An object value should behave like the kind of data it is meant to represent. For instance, by producing a string represnetation of itself.

- Strings are important: they represent language and programs.
- In python, all objects produce two string representations:
  - The *str* is legible to humans
  - The *repr* is legible to the Python interpreter
  - They are often the same, but not always.

### The repr String for an Object
The *repr* function returns a Python expression(a string) that evaluates to an equal object.
- repr(object) -> string
- return the canonical string representation of the object.
- for most obejct types, eval(repr(object)) == object.

The result of calling *repr* on a value is what Python prints in an interactive session
```python
>>> 12e12
12000000000000.0
>>> print(repr(12e12))
12000000000000.0
```

Some obeject do not have a simple Python-readable string
```python
>>> repr(min)
'<built-in function min>'
```

### The str String for an Obeject
Human interpretable strings are useful as well:
```python
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half)
'1/2'
>>>
```

The result of calling str on the value of an expression is what Python prints using the print function:
```python
>>> print(half)
1/2
```

### Demo
```python
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half)
'1/2'

>>> s = "Hello, World"
>>> s
'Hello, World'
>>> print(repr(s))
'Hello, World'
>>> print(s)            # print will unqoute the qoutes
Hello, World
>>> print(str(s))
Hello, World
>>> str(s)
'Hello, World'
>>> repr(s)             # repr will return the *string* of the exact expression
"'Hello, World'"
>>> repr(repr(repr(s)))
'\'"\\\'Hello, World\\\'"\''
```

## Polymorphic Functions
A function that applies to many (poly) different forms (morph) of data. *str* and *repr* are both polymorphic; they apply to any object.

*repr* invokes a zero-arugment method \__repr__ on its argument
```python
>>> half.__repr__()
'Fraction(1, 2)'
```
*str* invokes a zero-argument method \__str__ on its argument
```python
>>> half.__str__()
'1/2'
```

### Implementing repr
- An instance attribute called \__repr__ is ignored
- Only class attributes are found
```python
def repr(x):
    return type(x).__repr__(x)
```

### Implementing str
- An instance attribute called \__str__ is ignored
- If no \__str__ attribute is found, uses *repr* string
- *str* is a class, not a function
```python
>>> class Bear:
...     def __repr__(self):
...             return 'Bear()'
...
>>> oski = Bear()
>>> print(oski)
Bear()
>>> print(str(oski))
Bear()
>>> print(repr(oski))               # There is no qoutes.
Bear()
>>> print(oski.__str__())
Bear()
>>> print(oski.__repr__())
Bear()

>>> class Bear:
...     def __repr__(self):
...             return 'Bear()'
...     def __str__(self):
...             return 'a bear'
...
>>> print(oski)
a bear
>>> print(str(oski))
a bear
>>> print(repr(oski))
Bear()
>>> print(oski.__str__())
a bear
>>> print(oski.__repr__())
Bear()

>>> class Bear:
...     def __init__(self):
...         self.__repr__ = lambda: 'oski'
...         self.__str__ = lambda: 'this bear'
...     def __repr__(self):
...             return 'Bear()'
...     def __str__(self):
...             return 'a bear'
...
>>> print(oski)
a bear
>>> print(str(oski))
a bear
>>> print(repr(oski))
Bear()
>>> print(oski.__str__())
oski
>>> print(oski.__repr__())
a bear

# Implement str
def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)
```

## Interfaces
- **Message passing:** Objects interact by looking up attributes on each other (passing message)
- The attribute look-up rules allow different data types to respond to the same message
- A **shared message** (attribute name) taht elicits similar behavior from different object classes is a powerful method of abstraction
- An interface is a set of shared messages, along with a specification of what they mean

Eample: \__repr__ and \__str__ methods that return Python-interpretable and human-readable strings implement an interface for producing string representations.

## Special Method Name
- Certain names are special because they have built-in behavior
- These names always start and end with two underscores
| Name      | Behavior                                                   |
| --------- | ---------------------------------------------------------- |
| __init__  | Method invoked automatically when an object is constructed |
| __repr__  | Method invoked to display an object as a Python expression |
| __add__   | Method invoked to add one object to another                |
| __bool__  | Method invoked to convert an object to True or False       |
| __float__ | Method invoked to convert an object to a float             |
```python
>>> zero, one, two = 0, 1, 2
>>> one + two
3
>>> bool(zero), bool(one)
(False, True)
# Equals to
>>> zero, one, two = 0, 1, 2
>>> one.__add__(two)
3
>>> zero.__bool__(), one.__bool__()
(False, True)
```

### Adding "+"
Adding instances of user-defined classes invokes either the \__add__ or__radd__ method.
```python
class Ratio:
    def __init__(self, n, d):
        slef.numer = n
        slef.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):                                  # type dispatching
            n = self.numer + self.denom * other
            d = self.deon
        elif isinstance(other, Ration):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other                              # type coercion
        g = gcd(n, d)
        return Ratio(n//g, d//g)

    __radd__ = __add__                                              # 1 + Ratio(1, 3) now is the same as Ratio(1, 3) + 1

    def __float__(self):
        return self.numer/self.denom

def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d)
    return n
```

## Q&A
- 00:02​ Why does Prof. Farid not use object-oriented programming in his day-to-day programming?
  - In data processing and some other scenarios, there is not many mutations and changing states, so OOP may don't shine.
- 01:03​ What does it mean that str is a class and not a function?
- 02:12​ In the "Polymorphic Functions" video, repr and str are redefined after calls to print. Is that a mistake?
- 02:58​ How does addition interact with user-defined classes using \__add__ and \__radd__?
  - When python evaluates "x + y", it exams whether x is a user-defined class and sees if there's a \__add__ method, if not, it checks if y has a \__radd__ method.
- 05:01​ Could you use "in" instead of "for" to check the contents of a Kangaroo's pouch?
- 05:35​ Is isinstance(a, B) the same as type(a) == B?
  - Because of inheritance, there might be difference.
```python
>>> b = B()
>>> isinstance(b, B)
True
>>> isinstance(b, A)
True
>>> type(b)
<class '__main___.B'>
>>> type(b) == B
True
>>> type(b) == A
False
```
- 06:49​ What's the difference between repr and \__repr__?
  - You see them in different places. 
- 09:12​ Does every class define \__repr__?
  - Yes. If it's not defined, you will see sth like \<__main___.B object at 0xXXXXXXXXXX>
- 09:57​ How would you print all the paths from the root of a tree to one of its leaves?
  - yield [label(t)] + all branches' all paths
- 15:18​ How do you solve Fall 2015 Midterm 2 Question 3(a): d-k-complete trees?
  - d-k-complete trees must have k (d-1)-k-complete branches
- 23:31​ Why is it the case that repr(x) could be different from x.\__repr__()?
  - repr() will ignore the instance's \__repr__.
- 25:52​ When you print an object with a \__repr__ method, why don't you see the str-string instead of the repr-string?
  - Maybe it didn't have a \__str__. Default \__str__ is calling \__repr__.
- 27:08​ How do \__add__ and \__radd__ relate? Are they always equal?
  - \__add__ works in "x + 1", while \__radd__ works in "1 + x".

# Ch. 2.7
*generic function:* A function that can accept values of multiple different types.
- three techniques to implement it:
  - shared interfaces
  - type dispatching
  - type coercion

## Special Methods
### True and False Values. (Bool)
All objects in Python have a truth value. By default, user-defined classes are True. \__bool__ method can be used to override this behavior.
```python
>>> Account.__bool__ = lambda self: self.balance != 0
>>> bool(Account('Jack'))
False
```

### Sequence Operations
- *len* function invokes the \__len__ method of its argument.
- Python uses a sequence's length to determine its truth value.
- Selection operator [] invokes the \__getitem__ method.
```python
>>> len('Go Bears!')
9
>>> len('Go Bears!')
9

>>> bool('')
False
>>> bool([])
False
>>> bool('Go Bears!')
True

>>> 'Go Bears!'[3]
'B'
>>> 'Go Bears!'.__getitem__(3)
'B'
```

### Callable obejcts
Python also allows us to define objects that can be "called" like functions by including a \__call__ method.
```python
def make_adder(n):
        def adder(k):
            return n + k
        return adder
add_three = make_adder(3)
add_three(4)
7

class Adder(object):            # what is 'object' supposed to do?
        def __init__(self, n):
            self.n = n
        def __call__(self, k):  # This make Adder instances callable
            return self.n + k
add_three_obj = Adder(3)
add_three_obj(4)
7
```

### Arithmetic
Special methods can also define the behavior of built-in operators applied to user-defined objects. (overload)

For readers interested in further details, the Python documentation describes the exhaustive set of [method names for operators](https://docs.python.org/3/reference/datamodel.html#special-method-names). Dive into Python 3 has a chapter on special method names that describes how many of these [special method names](https://diveintopython3.net/special-method-names.html) are used.

## Multiple Representations
Data type might have multiple representations, as different scenarios have their own optimal representation (like Complex Number). In addition to the data-abstraction barriers that isolate *representation* from *use*, we need abstraction barriers that isolate different design choices from each other and *permit different choices* to coexist in a single program.
```python
"""Complex number is a kind of Number, numbers can + and *.

The purpose of Number is not to be instantiated directly, but instead to serve as a superclass of various specific number classes.
"""
class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)

""" Complex numbers' RI representation is optimal for add, while MA representation is optimal for mul
Here we assume:
- ComplexRI constructs a complex number from real and imaginary parts.
- ComplexMA constructs a complex number from a magnitude and angle.
"""
class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)
```
Here is what OOP shines.
- Interfaces. An interface is a set of *shared attribute names*, along with a *specification of their behavior*.
  - Idealy, RI's MA should be converted by RI repr, vice versa. So same names have different behaviors in the two.
- Properties. Two or more attribute values maintain a fixed relationship with each other is a new problem.
  - One solution is to one repr and compute when needed.
  - Python has a *@property* to allow function to be called without call expression. So properties' method look like attributes
```python
from math import atan2
class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    @property
    def angle(self):
        return atan2(self.imag, self.real)
    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

from math import sin, cos, pi
class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)
```
The interface is also *additive*. If another programmer wanted to add a third representation of complex numbers to the same program, they would only have to create another class with the same attributes.

## Generic Functions
Generic functions are methods or functions that apply to arguments of different types. By using shared interfaces, the Complex.add method is generic, because it can take either a ComplexRI or ComplexMA as the value for other.

There are other two ways to implement generic functions:
### Type Dispatching
Write functions that inspect the type of arguments they receive, then execute code that is appropriate for those types. Now we want to extend the Complex Number with Ration Number.
```python
Rational.type_tag = 'rat'           # type_tag is a general way to receive the type of an instance
Complex.type_tag = 'com'

def add_complex_and_rational(c, r): # a Rational can be converted to a float value
    return ComplexRI(c.real + r.numer/r.denom, c.imag)

def mul_complex_and_rational(c, r):
    r_magnitude, r_angle = r.numer/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

def add_rational_and_complex(r, c): # they are commutative
    return add_complex_and_rational(c, r)
def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)
```
The role of type dispatching is to ensure that these cross-type operations are used at appropriate times. Below, we rewrite the Number superclass to use type dispatching for its \__add__ and \__mul__ methods.
```python
class Number:
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)
    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):             # cross_fns is a dictionary 
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)

    adders = {("com", "rat"): add_complex_and_rational,
                ("rat", "com"): add_rational_and_complex}
    multipliers = {("com", "rat"): mul_complex_and_rational,
                    ("rat", "com"): mul_rational_and_complex}
```
New subclasses of Number could install themselves into the system by declaring a type tag and adding cross-type operations to Number.adders and Number.multipliers. (cross subclasses) They could also define their own adders and multipliers in a subclass. (in their own subclasses)

### Coersion
Coersion is a cross-type operation by attempting to coerce both arguments to the same type.
```python
def rational_to_complex(r):
    return ComplexRI(r.numer/r.denom, 0)
```
The alternative definition of the Number class performs cross-type operations by coercing another argument as Complex Number
```python
class Number:
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)
    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return self, other
        elif (self.type_tag, other.type_tag) in self.coercions: # a 2-element tuple is the key
            return (self.coerce_to(other.type_tag), other)A
        elif (other.type_tag, self.type_tag) in self.coercions:
            return (self, other.coerce_to(self.type_tag))
    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other_tag)]
        return coercion_fn(self)
    coercions = {('rat', 'com'): rational_to_complex}
```
Pro:
- appropriate transformation between types depends only on the types themselves (You don't need write two pairs)
- reduce the total number of coercion functions that are required by a program.
  -  coerce two different types each into a third common type. (rhombus, rectangle -> quadrilateral)
  -  iterative coercion, in which one data type is coerced into another via intermediate types.

Con:
- lose information when they are applied.
- Early versions of Python had a \__coerce__ special method on objects. In the end, the complexity of the built-in coercion system did not justify its use, and so it was removed.