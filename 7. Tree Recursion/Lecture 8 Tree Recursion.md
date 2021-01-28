# Lecture
## Inverse Cascade
```python
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, n, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
```

## Tree Recursion
Tree-shaped processes arise whenever executing the body of a recursive function makes more than one call to that function.

### Fibbonacci
```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
```

### 3 Pegs Hanoi:
```python
def solve_hanoi(n, start_peg, end_peg):
    if n == 1:
        move_disk(n, star_peg, end_peg)
    else:
        spare_peg = 6 - start_peg - end_peg)
        solve_hanoi(n-1, start_peg, spare_peg)
        move_disk(n, start_peg, end_peg)
        solve_hanoi(n-1, spare_peg, end_peg)
```

### Counting Partitions
The number of partitions of a positive integer n, using parts up to size m, is the number of ways in which n can be expressed as the sum of positive integer parts up to m in increasing order.
> count_partitions(6, 4)

Solve steps:
- Recursive decomposition: finding simpler instances of the problem.
- Explore two possibilities:
  - use at least one 4
  - don't use any 4
- Solve two simpler problems;
  - count_partitions(2, 4)
  - count_partitions(6, 3)
- Tree recursion often involves exploring different choices.

```python
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        return cout_partitions(n-m, m) + count_partitions(n, m-1)
    # you actually come up with recursive cases before base cases
```
