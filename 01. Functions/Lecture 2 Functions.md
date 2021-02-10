# Lecture 
## Evaluation procedure for all expression:
1. Evaluate the operator and then the operand subexpressions
2. apply the funciton that is the value of the operator subexpression to the arguments that are the values of the operand subexpression

> An expreesion describes a computation and evaluates to a value
> 
> Operators and operand are also expressions
### Primitive expressions
| 2      | add  | hello  |
| ------ | ---- | ------ |
| number | Name | String |

### Call expressions
| max      | (2,     | 3)      |
| -------- | ------- | ------- |
| operator | operand | operand |
> an operandd can also be a call expression

## Environment diagram
| Code                             | Frames                                   |
| -------------------------------- | ---------------------------------------- |
| statements and expressions       | each name is bund to a value             |
| arrows indicate evaluation order | wthin a frame, a name cannot be repeated |
> viusalize the program by using tutor
> "scope"

## execution rule for assignment statements:
1. evaluate all expressions to the right of "=" from left to right.
2. bind all names to the left of "=" to the resulting values in the current frame

## Defining functions
Assignment: binds names to values
Function: binds names to expressions.(a more powerful means of abstraction)
> remember this course is about abstraction

## excution procedure for def statements:
1. create a function with signature \<name>(\<formal parameters>)
2. set theh body of that function to be everything indented(what tab does) after the first line
   1. the body doesn't excute until the function was called (squirrel)
3. Bind \<name> to that function in the current frame (parent)

## Environment Diagrams for Nested Def Statements
- Every user-defined function has a parent frame (often global)
- The parent of a function is the frame in which it was defined
- Every local frame has a parent frame (often global)
- The parent of a frame is the parent of the function called
  
## Procedure for calling/applying user-defined functions (version 1):
1. add a local frame, forming a new environment(just like C run a function, an independent environment)
    ```
    global frame
    name | value
    ```
    ```
    local frame
    name | value
    ```
2. copy the parent of the function to the local frame: \[parent-\<label>]
3. bind the function's formal parameters to its arguments in that frame.
4. execute the body of the function in that new environment

> an environment is a sequencce of frames
> 
> a name evaluates to the value bound to that name in the *earliest frame* of the current environment in which that name is found. The earliest frame is found by its parent, if needed.
e.g. to look up some name

E.g., to look up some name in a function:
- look for that name in the local frame
- if not found, look for it in the global frame
> for a function, local frame is closer than global frame

# Ch. 1.1
## Statements & Expressions
Computer programs consist of instructions to either

1. Compute some value - Expressions
2. Carry out some action - Statements

## Functions
Functions encapsulatee logic that manipulaltes data

## Objects
An object seamlessly *bundles together* data and the *logic* that manipulates that data

## Interpreters
A program that implement evaluating compound expressions

> functions are objects, objects are functions, and interpreters are instances of both

## Debugging
1. test incrementally
   1. using small, modular components that can be tested individually.
   2. try components ASAP to identify problems

2. isolate errors
3. check your assumptions
4. consult others

# Ch 1.2
## mechanisms of languages
1. primitive expressions and statements: building blocks
2. means of combination
3. means of abstraction: elements can be named and manipulated as units

## Expressions
## Call Expressions
max(7.2, 9.5) - we say that the function *max* is called with *arguments* 7.5 and 9.5

Function notation advantages over infix notation:
1. No ambiguity, the function name always precedes its arguments
2. No limit to nesting
3. Easy to input

## Importing Library Functions
from \<lib> import \<module>

## Names and the Environment
- *environment*: memory that keeps track of the names, values, and bindings.
- name (variable(s))

```
>>> x, y = 3, 4.5
>>> y, x = x, y
>>> x
4.5
```

## Pure Function
Functions that only return a value. Same the arguments, same the value.
```
>>> print(print(1), print(2))
1
2
None None
```
### Benefits
1. reliably nested
2. simpler to test. same return value -> compared with expected return value
3. essential for writing *concurrent* programs
> concurrent: runs simultaneously with other concurrent programs