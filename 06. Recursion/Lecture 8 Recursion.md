# Lecture
Recursive Functions: A function is called recursive if the body of that function calls itself, either directly or indirectly.

## Iteration vs Recursion
<table>

<tr>
<td style="text-align: center; vertical-align: middle;"> While </td>
<td style="text-align: center; vertical-align: middle;"> Recursion </td>
</tr>

<tr>
<td> 

```python
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total*k, k+1
    return total
```

</td>
<td>

```python
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
```

</td>
</tr>

<tr>
<td> 

$$ n! = \prod_{k=1}^{n} k $$

</td>
<td>

$$
n! =
\begin{cases}
    1 & if \;\; n=0 \\
    n\cdot (n-1)! & otherwise
\end{cases}
$$

</td>
</tr>

<tr>
<td style="text-align: center; vertical-align: middle;">n, total, k, fact_iter</td>
<td style="text-align: center; vertical-align: middle;">n, fact</td>
</tr>

</table>

## Verifying Recursive Functions
Is *fact* implemented correctly?
1. verify the base case. (n=0)
2. Treat *fact* as a functional abstraction!
3. Assume that fact(n-1) is correct.
4. Verify that fact(n) is correct, in the base of 3.

## Mutal Recusion
### The Luhn Algorithm
```python
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(n) + luhn_digit
```

## Relationship between Recursion and Iteration
### Converting Recursion to Iteration
Iteration is a special case of recursion.

**Idea**: The state of an iteration can passed as arguments.
```python
def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum += last
    return digit_sum

def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)
```

## Q&A
### Difference between Self-reference and Recursion
Recursion will trigger a chain of computation (it will call itself), whereas self-reference only return a function that is itself.

# Ch. 1.7
## The Anatomy of Recursive Functions
### Character: they simplify the original problem
Recursive functions express computation by simplifying problems incrementally. 

The iterative function constructs the result from the *base case* of 1 to the final total by successively computation in each term. 

The recursive function constructs the result directly from the final term, n, and the result of the simpler problem, n-1.

Leap of faith: Treating a recursive call as a function abstraction, by which we should not care about how n-1 is implemented.

Iterative functions must maintain some local state that changes throughout the course of computation.

## Mutual Recursion
A recursive procedure is divided among two functions taht call each other.

Even or odd:
- a number is even if it's one more than an odd number
- a number is odd if it's one more than an even number
- 0 is even

```python
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
```
Mutually recursive functions can be turned into a single recursive function by breaking the abstraction boundary between the two functions:
```python
def is_even(n):
    if n == 0: # think about what we can do to n
        return True
    else: # deal with n - 1
        if (n-1) == 0:
            return False
        else:
            return is_even((n-1)-1)

def is_even(n): 
    """This logic is different from the above one
    1. a number is even if it's two more than an even number
    2. 0 is even
    3. 1 is odd
    It's more like a iteration rather recursion
    """
    if n == 0:
        return True
    elif n == 1:
        return False
    else
        return is_even(n-2)
```

## Printing in Recursive Functions
It's not a rigid requirement that base cases be expressed before recursive calls.
```python
def cascade(n):
    print(n)
    if n >= 10:
        casecade(n//10)
        print(n)
```

# Disc03
Three common steps in a recursive definition:
1. Figure out your base case: move on to the point that we can't reduce the problem any further.
2. Make a recursive call with a simpler argument: if we know what factorial(n-1) is, the problem will be much simpler.
3. Use your recursive call to solve full problem: now we can multiply factorial(n-1) by n to solve the problem

> internal correctness and not running forever (halting)