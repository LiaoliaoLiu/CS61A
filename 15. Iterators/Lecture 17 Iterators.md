# Lecture
## Iterators
An iterator can provide access to a container's elements in some oder.
```python
iter(iterable) # Return an iterator
next(iterable) # Return the next element in an iterator

>>> s = [[1,2],3,4,5]
>>> s
[[1, 2], 3, 4, 5]
>>> next(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator
>>> t = iter(s)
>>> next(t)
[1, 2]
>>> next(t)
3
>>> list(t)     # See what's left
[4, 5]          # Only contains the things that are not "nexted"
>>> next(t)     # You see what's left by "nexting" them
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration   # How python tells you you reached an end
```

## Iterators for Dictionary
- An iterable value is any value that can be passed to *iter* to produce an iterator
- An iterator is returned from *iter* and can be passed to *next*; all iterators are mutable
- A dictionary, its keys, its values, and its items are all iterable values
  - The order of items in a dictionary is the order in which they were added (python3.6+)
  - Arbitary (Python3.5 and earlier)

```python
>>> d = {'one':1, 'two':2}
>>> k = iter(d)
>>> next(k)
'one'
>>> d['zero'] = 0   # You can not change the size of the iterating obejct during iterating
>>> next(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
>>> d
{'one': 1, 'two': 2, 'zero': 0}
>>> k = iter(d)
>>> next(k)
'one'
>>> next(k)
'two'
>>> d['zero'] = 5   # But you can change the element
>>> next(k)
'zero'
```

## Built-in Functions for Iteration
Many built-in Python sequence operations return iterators that compute results lazily. (compute only when you call them)
| Function                       | Behavior                                      |
| ------------------------------ | --------------------------------------------- |
| map(func, iterable):           | Iterate over func(x) for x in iterable        |
| filter(func, iterable):        | Iterate over x in iterable if func(x)         |
| zip(first_iter, second_iter): | Iterate over co-indexed (x, y) pairs          |
| reversed(sequence):            | Iterate over x in a sequence in reverse order |

To view the contents of an iterator, place the resulting elements into a container
| Function          | Behavior                                  |
| ----------------- | ----------------------------------------- |
| list(iterable):   | Creat a list containing all x in iterable |
| tuple(iterable):  | Creat a tuple ...                         |
| sorted(iterable): | Creat a sorted list ..                    |

```python
def double(x):
    print('**', x, '==>', 2*x, '**')
    return 2*x

>>> m = map(double, range(3, 7))
>>> f = lambda y: y >= 10
>>> t = filter(f, m)
>>> next(t)
** 3 ==> 6 **
** 4 ==> 8 **
** 5 ==> 10 **  # Find the first iterable
10
>>> next(t)
** 6 ==> 12 **
12
>>> list(t)
[]
>>> list(filter(f, map(double, range(3,7))))
** 3 ==> 6 **
** 4 ==> 8 **
** 5 ==> 10 **
** 6 ==> 12 **
[10, 12]
```

## Generators and Generator Functions
- A *generator function* is a function that *yield*s values instead of *return*ing them. (like interrupt)
- A normal function *return*s once; a generator function can *yield* multiple times. (lazy computation)
- A *generator* is an iterator created automatically by calling a *generaotr function*.
- When a *generator function* is called, it returns a *generator* that iterates over its *yields*.

```python
def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

>>> t = evens(2, 10)
>>> next(t)
2
>>> next(t)
4
>>> next(t)
6
>>> next(t)
8
>>> next(t)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> list(evens(1,10))
[2, 4, 6, 8]
```

### *yield from* Statement
A *yield from* statement yields all values(one at a call) from an iterator or iterable. It evaluates the expression first, so the expression must evaluate to a generator.
```python
def prefixes(s):
    if s:
        yield from prefixes(s[:-1]) # It DOESN'T yield anything directly
        yield s                     # The program pauses and waits for next call after this line

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

>>> list(prefixes('both'))
['b', 'bo', 'bot', 'both']
>>> list(substrings('tops'))
['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
```

## Q&A
- 00:03​ What is the relationship between "yield from" and a for statement that yields?
  - "yield from" is just a convienience. It can always be replaced by for statement
- 02:27​ Do you always need a yield after a "yield from" statement?
  - Literally, No. But you need it to work well in this example.
- 02:54​ What does prefixes(s[:-1]) evaluate to in the prefixes example from lecture?
  - Consequently 'b', 'bo', 'bot'.
- 03:38​ Why does removing the yield statement in prefixes cause the function not to yield anything?
  - Put one character to the function see the base case. The function didn't do anything.
- 05:03​ If an iterator is not a list, then what is it?
  - PS: Regard iterator as a linked list of pointers with behaviors you know.
- 06:25​ When should you use built-in Python features instead of reimplementing them?
  - Reimplementing is mostly for compatibility.
- 09:34​ What happens if you reverse the order of "yield" and "yield from" in the prefixes example?
  - ['both', 'bot', 'bo', 'b']
- 11:45​ Why do you need to "yield from" the recursive call to countdown instead of just yielding it?
  - You got a generator for the iterator. ['both', \<generator>]
- 13:30​ Why does calling list on an iterator twice return an empty list the second time?
  - Iterator "used up".
- 16:30​ What are the practical applications of yield, rather than just returning?
  - Lots of cases when your program is interacting with sth, to save the time of get "list": decompressing a few frames in a video.
- 19:10​ Is it true that a generator is always an iterator, but an iterator is not always a generator?
  - A generator is a more specific iterator.
- 19:53​ How would you solve the Summer 2020 Midterm Question 2?
  - galaxy problem.
- 28:50​ Is a for statement just building an iterator and then calling next on it?
  - Behavior is identical.
- 29:33​ Is there any way to reset an iterator to its original position?
  - No, you need make a new one.
- 30:28​ Do "yield from" statements have to make recursive calls?
  - There is no direct relation.
- 32:01​ Can yield be used within a larger expression?
  - No, just like return.
- 32:46​ Can you do more than one thing in the body of a list comprehension?
  - Only one expression. But the expression might do what you want.
- 33:52​ How does new content get added to an iterator after some other code has already started consuming the iterator?
  - Like 'reverse the order of "yield" and "yield from"', you can creat the iterator after you consumed one and use the new iterator.

# Ch. 4.2 Implicit Sequence
An implicit Sequence is a sequence made by lazy computation, in which an element is computed when it was required. An Explicit Sequence will store each emelent in the memory.

## Iterators
While not as flexible as accessing arbitrary elements of a sequence (called random access), sequential access to sequential data is often sufficient for data processing applications.

## Iterables
Any value that can produce iterators is called an iterable value. In Python, an iterable value is anything that can be passed to the built-in iter function.

## For Statements in View of Iterators
To execute a for statement:
1. Python evaluates the header \<expression>, which must yield an iterable value. 
2. the \__iter__ method is invoked on that value. 
3. Python invokes the \__next__ method on that iterator and binds the result to the \<name> in the for statement, until a StopIteration exception is raised
4. it executes the \<suite>.
5. repeat 3. 4.

```python
>>> counts = [1, 2, 3]
>>> for item in counts:
        print(item)
1
2
3

>>> items = counts.__iter__()
>>> try:
        while True:
            item = items.__next__()
            print(item)
    except StopIteration:
        pass
1
2
3
```

If you iterate over a list, but change the contents of that list at the same time, you may not [visit all the elements](https://docs.python.org/3/tutorial/controlflow.html#for-statements).
## Generawtors and Yield Statements
Generators do not use attributes of an object to track their progress through a series. Instead, they control the execution of the generator function, which runs until the next yield statement is executed each time the generator's \__next__ method is invoked.

A generator object has \__iter__ and \__next__ methods, and each call to \__next__ continues execution of the generator function from wherever it left off previously until another yield statement is executed.

We can walk through the generator by manually calling \___next__():
```python
>>> letters = letters_generator()
>>> type(letters)
<class 'generator'>
>>> letters.__next__()
'a'
>>> letters.__next__()
'b'
>>> letters.__next__()
'c'
>>> letters.__next__()
'd'
>>> letters.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
The generator does not start executing any of the body statements of its generator function until the first time \__next__ is invoked. The generator raises a StopIteration exception whenever its generator function returns.

## Iterable Interface
An object is iterable if it returns an iterator when its \__iter__ method is invoked. Iterable values represent data collections, and they provide a fixed representation that may produce more than one iterator (Think about iter(\<iterable>)).
```python
>>> class Letters:
        def __init__(self, start='a', end='e'):
            self.start = start
            self.end = end
        def __iter__(self):
            return LetterIter(self.start, self.end)

>>> b_to_k = Letters('b', 'k')
>>> first_iterator = b_to_k.__iter__()
>>> second_iterator = iter(b_to_k)
>>> first_iterator is second_iterator
False
>>> first_iterator.__next__() == second_iterator.__next__()
True
# This is what "more than one iterator" means. The two methods are identical in terms of creating an iterator.
```
The iterator tracks progress through sequential data, while an iterable represents the data itself.

### Creating Iterables with Yield
If an iterable object returns a fresh instance of an iterator each time \__iter__ is called, then it can be iterated over multiple times. (remember the LetterIter function's implementation in the previous section is unkown)
```python
>>> class LettersWithYield:
        def __init__(self, start='a', end='e'):
            self.start = start
            self.end = end
        def __iter__(self):
            next_letter = self.start                  # That's how you implement the LetterIter you *want*
            while next_letter < self.end:
                yield next_letter
                next_letter = chr(ord(next_letter)+1)
```

## Iterator Interface
Typically, an iterator is not reset; instead a new instance is created to start a new iteration.
```python
>>> class LetterIter:
        """An iterator over letters of the alphabet in ASCII order."""
        def __init__(self, start='a', end='e'):
            self.next_letter = start
            self.end = end
        def __next__(self):
            if self.next_letter == self.end:      # You can creat a infinite iterator like positive
                raise StopIteration
            letter = self.next_letter
            self.next_letter = chr(ord(letter)+1)
            return letter
```

## Python Streams
You can image Streams as lists, but a stream stores how to compute the rest of the stream, rather than always storing the rest explicitly.
```python
class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:        # When the rest attribute is requested via a dot expression,
            self._rest = self._compute_rest()     # the rest property method is invoked, which triggers this computation
            self._compute_rest = None             # Compute, then discard
        return self._rest                         # The underscore indicates it should not be accessed directly
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

>>> r = Link(1, Link(2+3, Link(9)))
>>> s = Stream(1, lambda: Stream(2+3, lambda: Stream(9)))
# The essential properties of a compute_rest function are that it *takes no arguments*, and it returns a *Stream* or *Stream.empty*. 
>>> r.rest
Link(5, Link(9))
>>> s.rest
Stream(5, <...>)
``` 

Lazy evaluation gives us the ability to represent infinite sequential datasets using streams.
```python
def integer_stream(first):
    def compute_rest():
        return integer_stream(first+1)      # It returns an initialized *Stream*
    return Stream(first, compute_rest)      # Call it lazy bacuse compute_rest is called only when *rest* is required


>>> positives = integer_stream(1)
>>> positives
Stream(1, <...>)
>>> positives.first
1
```

Imaging a post-filted stream(like a list) can help you under *filter_stream* quickly. It was archieved by recursively so don't bother to think imperatively, instead, think recursively.
```python
def filter_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()


>>> def primes(pos_stream):
        def not_divible(x):
            return x % pos_stream.first != 0
        def compute_rest():
            return primes(filter_stream(not_divible, pos_stream.rest)) # Leap of faith here, thinking imperatively only f**cks you up
        return Stream(pos_stream.first, compute_rest)

>>> prime_numbers = primes(integer_stream(2))
>>> first_k_as_list(prime_numbers, 7)
[2, 3, 5, 7, 11, 13, 17]
```

# Disc06
## Nolocal
However, there are two important caveats with nonlocal names:
- A variable declared nonlocal must be dened in a parent frame which is not the global frame.
- Names in the current frame cannot be overridden using the nonlocal keyword. This means we cannot have both a local and nonlocal binding with the same name in a single frame.

Because nonlocal lets you modify bindings in parent frames, we call functions that use it mutable functions.

## Iterators
In general, any object that can be iterated over in a for loop can be considered an iterable.

the relationship between an iterable and an iterator is analogous to the relationship between a book and a bookmark - an iterable contains the data that is being iterated over, and an iterator keeps track of your position within that data.

Note that most iterators are also iterables - that is, calling iter on them will return an iterator. This means that we can use them inside for loops. However, calling iter on most iterators will *not* create a new iterator - instead, it will simply return the same iterator.

## Generators
- When a generator function is called, it returns a generator object, which is a type of iterator. It doesn't execute the body.
- Return statement closes the current frame after the function exits, a yield statement causes the frame to be saved until the next time next is called
- Once next is called again, execution resumes where it last stopped and continues until the next yield statement is executed or the end of the function. 
- A generator function can have multiple yield statements.
- Python recognize generator functions by yield statement.