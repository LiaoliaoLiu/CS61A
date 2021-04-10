# Lecture
## Non-Local Assignment & Persistent Local State
Convention: put nonlocal statement in the top of the function.

## The Effect of Nonlocal Statements
    nonlocal <name>, <name>, ...

*Effect*: Future assignments to that name change its pre-existing binding in the *first non-local frame* of the current environment in which name is bound.

### Python 3 language reference:
- Name listed in a nonlocal statement must refer to pre-existing bindings in an enclosing scope.(first non-local frame)
- Name listed in a nonlocal statement must not collide with pre-existing bindings in the local scope. (current frame)

## Mutable Values & Persistent Local State
Mutable values can be changed *without* a nonlocal statement.
```python
def make_withdraw(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw
```

## Referential Transparency, Lost
Expressions are referentially transparent if substituting an expression with its value does not cahnge the meaning of a program.
```python3
mul(add(2, mul(4,6)), add(3,5))
mul(add(2,    24    , add(3,5)))
```
Mutation operations *violate* the condition of referential transparency beacuse they do more than just return a value; *they change the environment.*

## Q&A
### 00:03​ Is Nonlocal assignment used much in practice?
### 01:56​ When a list refers to itself, how does that work? 
### 05:05​ How do you solve a tree problem that involves two labels for nodes that aren't next to each other?
parent_used restricts both parents and children.
### 07:53​ How do you solve Q1 of Quiz 4 from the exam prep section?
### 17:40​ Why when you assign to a local name that is the same as a nonlocal name, you get an error when referencing the nonlocal name?
### 23:04​ how do you solve Q7 of Summer 2020 Midterm 2?
using graft function to append new structures.
### 33:41​ What's the difference between adding two lists together and using append?
```python
c = a
a = a + b # c point directly to the object

c = a
a += b # c point to the a
```

# Ch. 2.4
## Programming Pattern: Dispatch Function
    dispatch(message, behavior_arg)
The message determines the behavior of the function, and the additional arguments are used in that behavior.

## Message Passing
The discipline that encapsulates the logic for all operations on a data value within one function that responds to different messages, is called message passing.

## [Propagating Constraints](http://composingprograms.com/pages/24-mutable-data.html)
The book used Fahrenheit and Celsius temperatures convertion to illustrate the *Constraint System*, which to me is a programming template to archieve 'equation'. I had a cursory look in the implementation. Maybe I should go back to the chapter when I need this.

