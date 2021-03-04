# Lecture
## Memoization
Remember the results that have been computed before.
```python
def memo(f):
    cache =  {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def count(f):
    # counted.call_count = 0 you cannot put it here
    def counted (n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0              # Fucntions can have attributes. IDK exactly why.
    return counted

>>> fib = count(fib)
>>> counted_fib = fib
>>> fib = memo(fib)
>>> fib = count(fib)
>>> fib(30)
832040
>>> fib.call_count
59
>>> counted_fib.call_count
31
```

## Exponentiation
```python
def exp(b, n):
# Linear time: Double the input doubles the time
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)

def exp_fast(b, n):
# Logarithmic time: Double the input increases the times by a constant C
    if n == 0:
        return 1
    else n % 2 == 0:    # 1024x the input increases the time by 10 which is log(2, 1024)
        return square(exp_fast(b, n//2))
    else:
        return b * exp_fast(b, n-1)
```

## Common Orders of Growth
Exponential growth
- recursive fib
- Incrementing $n$ *multiplies* times by a constant $b$ (Incrementing input multiplies resources)
- $a*b^{(n+1)} = a*b^n * b$
- $\Theta(b^n)$ (at least and at most)
- $O(b^2)$ (at most, aka, upper bound)

Quadratic growth
- overlap
- Incrementing $n$ *increases* times by n times a constant $a$ (Incrementing input adds n resources)
- $a*(n+1)^2 = a*n^2 + a*(2n+1)$
- $\Theta(n^2)$

Linear growth
- recursive exp
- Incrementing $n$ increase time by a constant $a$ (Incrementing input increments resources)
- $a*(n+1) = a*n + 1$
- $\Theta(n)$

Logarithmic growth
- exp_fast
- Doubleing $n$ only increment time by a constant (Multiplying input increments resources)
- $a*ln(2*n) = a*ln(n) + a * ln2$
- $\Theta(logn)$

Constant growth
- Increasing n doesn't affect time (Growth is independent of the input)
- Python dict key searching
- $\Theta(1)$

## The Consumption of Space
Active environments:
- Environments for any function calls currently being evaluated
- Parent environments of functions named in active environments

All other frame will be recycled.

## Q&A
- 00:03​ Explain function attributes
  - a function is also an object. Objects can be flexiblely given an attribute in python.
- 01:45​ Does the space complexity of recursive functions make them undesirable?
  - Tail recursion can be written in iterative version. If you found space complexity is a concern, you should consider if you need the recursion version. Recursion shines when you are handling problem like traverse a tree.
- 06:04​ Explain Exam Prep 6 Q 2: Linked lists Party and Costume
  - Link repr return 'Link(' + repr(self.first) + repr_rest + ')'

# Ch. 2.8
## Measuring Efficiency
- An environment becomes inactive whenever the function call (for which) its first frame was created finally returns.
- In general, the space required for tree-recursive functions will be proportional to the maximum depth of the tree.
- To summarize, the space requirement of the fib function, measured in active frames, is one less than the input, which tends to be small. The time requirement measured in total recursive calls is larger than the output, which tends to be huge.

## Orders of Growth
```python
from math import sqrt
def count_factors(n):
    sqrt_n = sqrt(n)
    k, factors = 1, 0
    while k < sqrt_n:
        if n % k == 0:
            factors += 2
        k += 1
    if k * k == n:
        factors += 1
    return factors
```

### Theta Notation
- $n$: parameter that measures the size of the input to some process, e.g., digits of accuracy.
- $R(n)$: the amount of some resource that the process requires for an input of size $n$.

We say that $R(n)$ has order of growth $Θ(f(n))$ (has $Θ(f(n))$ growth), written $R(n)=Θ(f(n))$ (pronounced "theta of $f(n)$"), if there are positive constants $k_1$ and $k_2$ independent of $n$ such that:
$$k_1 \cdot f(n) \leq R(n) \leq k_2 \cdot f(n)$$
for any value of $n$ larger than some minimum $m$.

> The expresions aside to the inequality are the bounds.

## Growth Categories
Orders of growth are designed to simplify the analysis and comparison of computational processes.

**Constants**. Constant terms do not affect the order of growth of a process. So, for instance, $Θ(n)$ and $Θ(500⋅n)$ are the same order of growth. This property follows from the definition of theta notation, which allows us to choose arbitrary constants $k_1$ and $k_2$ (such as $\frac{1}{500}$) for the upper and lower bounds. For simplicity, constants are always omitted from orders of growth.

**Logarithms**. The base of a logarithm does not affect the order of growth of a process. For instance, $log_2 n$ and $log_{10}n$ are the same order of growth. Changing the base of a logarithm is equivalent to multiplying by a constant factor.

**Nesting**. When an inner computational process is repeated for each step in an outer process, then the order of growth of the entire process is a product of the number of steps in the outer and inner processes. For example, the inner process requires $Θ(n)$ times, the outer process requires $Θ(m)$ times, then the total order of growth for this function is Θ(m⋅n).

**Lower-order terms**. lower-order terms are always omitted from orders of growth, and so we will never see a sum within a theta expression. $Θ(n2+k⋅n)$ and $Θ(n^2)$ are equivalent for any constant $k$ because the $n^2$ term will eventually dominate the total for any $k$. The fact that bounds must hold only for $n$ greater than some minimum $m$ establishes this equivalence.

Other categories exist, such as the $Θ(\sqrt{n})$ growth of count_factors.