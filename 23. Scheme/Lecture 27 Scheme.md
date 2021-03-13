# Lecture
Scheme is a Dialect of Lisp.
## Scheme Fundamentals
Scheme programs consist of expressions, which can be:
- Primitive expressions: 2, 3.3, true, +, quotient, ...
- Combinations: (quotient 10 2), (not true), ...
```scheme
> (quotient 10 2) ; numbers are self-evaluating, symbols are bound to values
5
> (+ (* 3
        (+ (* 2 4)
           (+ 3 5)))
     (+ (- 10 7)
        6))       ; Call expressions include an operator and 0 or more operands in parentheses
```

## Special Forms
A combination that is not a call expression is a special form:
- **If** expression:        (if \<predicate> \<consequent> \<alternative>)
- **And** and **or**:       (and \<e_1> ... \<e_n>), (or \<e_1> ... \<e_n>)
- Binding symbols:          (define \<symbol> \<expression>)
- New procedures:           (define (\<symbol> \<formal parameters>) \<body>)
```scheme
(define (sqrt x)
    (define (update guess)
        (if (= (square guess) x)
            guess
            ( update (average guess (/ x guess)))))
    (update 1)
```

## Cond & Begin
```scheme
(cond ((> x 10) (print 'big))
      ((> x 5)  (print 'medium))
      (else     (print 'small)))
; It's the same as below because the evaluation of cond in scheme
(print
    (cond ((> x 10) 'big)
          ((> x 5)  'medium)
          (else     'small)))
; You can only put one expresion in after the <predicate>
; That's why you need begin to combines multiple expressions into one expression
(if (> x 10) (begin
                (print `big)
                (print 'guy))
             (begin
                (print 'small)
                (print 'fry)))
```
## Let Expressions
```py
a = 3
b = 2 + 2
c = math.sqrt(a * a + b * b)
# a and b are still bound down here
```
```scheme
(define c (let ((a 3)
                (b (+ 2 2)))
               (sqrt (+ (* a a) (* b b)))))
; a and b are not bound down here
```

## Scheme Lists
- cons: Two-argument procedure that creates a linked list
- car: Procedure that returns the first element of a list
- cdr: Proccedure that returns the rest of a list
- nil: The empty list
> Scheme lists are writtern in parentheses with elements separated by spaces
```scheme
scm> (cdr (list 1 2 3 4))
(1 2 3 4)
```

## Symbolic Programming
Symbols normally refer to values; how do we refer to symbols?
```scheme
> (define a 1)
> (define b 2)
> (list a b)
(1 2)
```
Quotation is used to refer to symbols directly in Lisp.
```scheme
> (list 'a 'b)
(a b)
> (list 'a b)
(a 2)
```
Quotation can also be applied to combinations to form lists.
```scheme
> '(a b c)
(a b c)
> (car '(a b c))
a
> (cdr '(a b c))
(b c)
```

## A Scheme Expression is a Scheme List
The built-in Scheme list data structure (which is a linked list) can represent combinations
```scheme
scm> (list 'quotient 10 2)
(quotient 10 2)
scm> (eval (list 'quotient 10 2))
5
```
It's straightforward to write a program that writes a program. This's the reason why it is popular in AI.

## Generating Code
### Quasiquotation
There are two ways to quote an expression:
- Qoute:        '(a b) => (a b)
- Quasiquote:   `(a b) => (a b)

They are different because parts of a quasiquoted expression can be unquoted with ,
    
    (define b 4)

- Quote:        '(a ,(+ b 1)) => (a (unquote (+ b 1)))
- Quasiquote:   `(a ,(+ b 1)) => (a 5)

Quasiquotation is particularly convenient for generating Scheme expressions: You can choose which part to evaluate
```scheme
(define (make-add-procedure n) `(lambda (d) (+ d ,n)))
(make-add-procedure 2) => (lambda (d) (+ d 2))
```

### Example: While Statement
```scheme
(define (sum-while initial-x condition          add-to-total update-x)
;       (sum-while 1         '(< (* x x) 50)    'x           '(+ x 1))
;   v behold the quasiquote
    `(begin
        (define (f x total)
            (if ,condition
                (f ,update-x (+ total ,add-to-total))
                total))
        (f ,initial-x 0)))

scm> (define result (sum-while 1 '(< (* x x) 50) 'x '(+ x 1)))
(begin (define (f x total) (if (< (* x x) 50) (f (+ x 1) (+ total x)) total)) (f 1 0))
scm> (eval result)
28
```

## Q&A
- 00:03​ Do parentheses always form call expressions except when a quote converts the call expresion into a list?
  - Yes. '(f 2 3) => (list 'f 2 3)
- 01:10​ How do you write a procedure that sums all of the even elements in a list?
- 06:41​ How can you define a procedure without using lambda?
  - If you put a parenthesis after define, you make a procedure, if it's only a symble, then it will be a binding.
- 07:46​ How can you build a list out of an existing list?
- 10:47​ Are symbols different from strings?
  - Yes, strings in scheme are using double quotes. 
- 13:30​ What's the relationship between unquoting in Scheme and the repr function in Python?
  - Unquoting will directly evaluate the symbol. In the example, it evaluates to another symbol ('symbol), more like a string with variable in it. While repr you only gives your the expression without evaluating it.
- 14:13​ In Python can you generate code through something like quotation?
  - Python can eval a string and act like scheme, lots of other languages cannot do that.
- 16:02​ What does (print 1) evaluate to in Scheme?
  - You should never use the undefined values. It is determined by interpreter, which will easily change and be different in all kinds of scheme.
```scheme
scm> (define s (print 1))
1
s
scm> s
scm> (print s)
undefined
```
- 17:24​ Is undefined a true or false value?
- 18:36​ What happens when you call (lambda (foo x y z) (if x y z)) on a true value, a number and the result of a call to print?
- 21:35​ How do you evaluate an expression that has been quoted?
  - (eval '(+ 2 1))
- 23:14​ Can you evaluate using comma instead?
- 24:42​ Is there non-local assignment in Scheme?
  - (set! balance (- balance amount)) Remember this is a mutation. You lose referential transparency
- 27:54​ Do you need to know all the different equality testing procedures in Scheme?