# Lecture
## Functional Programming
- All functions are pure functions.
- No re-assignment and no mutable data types.
- Name-value bindings are permanent.
- Advantages of funtcional programming:
  - The value of an expression is independent of the order in which sub-expressions are evaluated.
  - Sub-expressions can safely be evaluated in parallel or on demand (lazily).
  - *Referential transparency:* The value of an expression does not change when we substitute one of its subexpression with the value of that subexpression.
- But... no for/while statements! We need use tail recursion to make basic iteration efficient.

## Recursion and Iteration in Python
In python, recursive calls always create new active frames.
```py
def factorial(n, k):
    if n == 0:
        return k
    else
        return factorial(n-1, k*n)  # even this is a tail recursion, python will save the current frame until it finaly returns
```

## Tail Recusion
> Implementations of Scheme are required to be *properly tail-recursive.* This allows the execution of an iterative computation in constant space, even if the iterative computation is described by a syntactically recursive procedure.
>
> -- Algorithmic Language Scheme

## Tail Calls
A procedure call that has not yet returned is *active*. Some procedure calls are *tail calls*. A Scheme interpreter should support an *unbounded number* of active tail calls using only a *constant* amount of space.

A tail call is a call expression in a tail context:
- The last body sub-expression in a tail context
- Sub-expressions 2 & 3 in a tail context *if* expression
- All non-predicate sub-expressions in a tail context *cond*    # retain the cond environment
- The last sub-expression in a tail context *and* or *or*       # retain the and/or environment
- The last sub-expression in a tail context *begin*

A call expression is not a tail call if more computation is still required in the calling procedure.
```Scheme
(define (length s)
    (if (null? s) 0
        (+ 1 (length (cdr s))))) ;because of (+ 1 expr), expr is not in a tail context
```

Linear recursive procedures can often be re-written to use tail calls.

The return value of the tail call is the return value of the current procedure call. Therefore, tail calls shouldn't increase the environment size.

### Example: Reduce
```Scheme
(define (reduce procedure s start)
    if (null? s) start
        (reduce procedure                   ; Recursive call is a tail call
            (cdr s)
            (procedure start (car s))))     ; Other calls are not; constant depends on whether procedure requires constant space
```

### Exampl: Map
```scheme
; non-tail-recursive version
(define (map produce s)
    (if (null? s)
        nil
        (cons (procedure (car s)) (map procedure (cdr s)))))

; tail-recursive version
(define (map procedure s)
    define (map-reverse s m)
        (if (null? s)
            m
            (map-reverse (cdr s)
                (cons (procedure (car s) m))))
    (reverse (map-reverse s nil))) ; now map-reverse is tail recursive, whether the function is tail recursion depends on reverse

(define (reverse s)
    (define (reverse-iter s r)
        (if (null? s)
            r
            (reverse-iter (cdr s) (cons (car s) r))))
    (reverse-iter s nil))
```

## Q&A
- 00:27​ What's the difference between a tail context and a tail call?
  - The tail context is the expression decides the return value (this decides whether the expression is *in* tail context )that meet the tail call definition.
- 03:32​ When does the code.cs61a.org SQL interpreter display a user-defined table?
- 04:05​ When do you need to join a table with itself and another table?
- 07:07​ What's the order of operations in a SQL query?
  - The SQL engine will decide which operation evaluates first in order to evalute other operations.
```SQL
SELECT name FROM cities WHERE latitude > 38; -- FROM -> WHERE -> SELECT
SELECT name, latitude > 38 AS cold FROM cities WHERE cold; -- FROM -> SELECT -> WHERE
```