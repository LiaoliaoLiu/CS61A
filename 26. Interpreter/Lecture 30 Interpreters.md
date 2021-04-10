# Lecture
## Interpreting Scheme
### The Structure of an Interpreter
*Compare with Calculator*
**Eval**
- Base cases:
  - Primitive values (numbers)
  - *Look up values bound to symbols*
- Recursive calls:
  - Eval(operator, operands) of all expressions
  - Apply(procedure, arguments)
  - *Eval(sub-expressions) of special forms*

> Requires an environment for symbol lookup

**Apply**
- Base cases:
  - Built-in primitive procedures
- Recursive calls:
  - *Eval(body) of user-defined procedures

> Creates a new environment each time a user-defined procedure is applied

### Scheme Evaluation
The *scheme_eval* function dispatches on expression form:
- Symbols are bound to values in the current environment.
- Self-evaluating expressions are returned.
- All other legal expressions are represented as Scheme lists, called *combinations*.

### Logical Special Forms
Logical forms may only evaluate some sub-expressions.
- **if** expression
- **and** and **or**
- **cond**

The value of an **if** expression is the value of a sub-expression.
- *do_if_form*
  - Evaluate the predicate
  - Choose a sub-expression: \<consequent> or \<alternative>
- Eval the sub-expression in place of the whole expression. (*scheme_eval*)

### Quotation
- The **quote** special form evaluates to the quoted expression, which is **not** evaluated.
- The \<expression> itself is the value of the quoted expression.
- '\<expression> is shorthand for (quote \<expression>).
  - The *scheme_read* parser converts shorthand to a combination.

### Lambda Expressions
Lambda expressions evaluate to user-defined procedures.
```py
class LambdaProcedure:
    def __init__(self, formals, body, env):
        self.formals = formals  # A scheme list of symbols
        self.body = body        # A scheme expression
        self.evn = evn          # A Frame instance
```

#### Frames and Environments
- A frame represents an environment by having a parent frame.
- Frames are Python instances with methods **lookup** and **define**.
- In Project 4, Frames do not hold return values.
```py
>>> 2+2
4
>>> Frame
<class '__main__.Frame'>
>>> scheme_eval
<function scheme_eval at ...>
>>> g = Frame(None)
>>> g
<Global Frame>
>>> f1 = Frame(g)
>>> f1
<{} -> <Global Frame>>
>>> g.define('x', 3)
>>> g.lookup('x')
3
>>> f1.define('x', 4)
>>> f1
<{x: 4} -> <Global Frame>>
>>> f1.lookup('x')
4
```
### Define Expressions
Define binds a symbol to a value in the first frame of the current environment.
1. Evaluate the \<expression>.
2. Bind \<name> to its value in the current frame.
```scheme
(define x (+ 1 2)) ==> (define x 3)
```
Procedure definition is shorthand of define with a lambda expression.
```scheme
(define (<name> <formal parameters>) <body>)

(define <name> (lambda (<formal parameters>) <body>))
```

#### Applying User-Defined Procedures
To apply a user-defined procedure,
- create a new frame in which formal parameters are bound to argument values,
- whose parent is the **env** of the procedure
> Evaluate the body of the procedure in the environment that starts with this new frame.

## Q&A
- 01:53​ Explain the diagram in Lab 11
- 05:42​ When should you quote arguments in a call expression and when should you leave them unquoted?
  - It depends on you want transfer is the symbol itself or what the symbol binds to.
- 09:38​ Why do we use a Frame class for Scheme instead of just using Python frames?
  - You cannot really do anything about Python frames using the python interpreter notion of frame, so we use dictionaries.
- 12:40​ How do you look up non-local symbols in Scheme?
  - Environment diagram.
- 14:13​ Is there non-local lookup in Scheme?

## Ch. 3.5 Interpreters for Languages with Abstraction
### Structure
1. Parsing
2. Evaluation
3. Procedure application
4. Eval/Apply Recursion

This mutually recursive structure, between an eval function that processes expression forms and an apply function that processes functions and their arguments, constitutes the essence of the evaluation process.