# Lecture
## Inheritance
- In heritance is a method for relating classes together.
- A common use: Two similar classes differ in their degree of specialization
- The specialized class may have the same attributes as the general class, aloong with some special-case behavior.
```python
class <name>(<base class>):
    <suite>
```
- The new subclass "shares" attributes with its base class. (attributes might be overrided)

### Looking Up Attribute Nanmes on Classes
Base class attributes aren't copied into subclasses:
1. If it names an attribute in the class, return the attribute value.
2. Otherwise, look up the name in the base class, if there is one.

## Object-Oriented Design
### Designing for Inheritance
- Don't repeat yourself; use existing implementations.
- Attributes that have been overridden are still accessible via class object.
```python
class CheckingAccount(Account):
    ...
    def with(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
```

### Inheritance and Composition
Object-oriented programming shines when we adopt the metaphor.
- Inheritance is best for representing *is-a* relationships.
  - a checking account *is a* specific type of account.
  - So, CheckingAccount inherits from Account.
- Composition is best for representing *has-a* relationships.
  - a bank *has a* collection of bank accounts it manages.
  - So, Bank has a list of accounts as an attribute.
```python
class Bank:
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind=Account): # kind here represents Composition
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
```

### Inheritance and Attribute Lookup
```python
class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.y(y)  # Here is the trick part, watch which class the "self" is
        else:                   # b.z is an B instance, b.z.z is a C instance,
            self.z = C(y+1)

class C(B):
    def f(self, x):             # b.z.z.z is 1. b.z.z.z.z will return an error (b.z.z.z evaluates to an integer)
        return x

a = A()
b = B(1)
b.n = 5
```

### Multiple Inheritance
CleverBank marketing executive wants:
- Low interest rate of 1% (already is in CheckingAccount)
- A $1 fee for withrawals (as above)
- A $2 fee for deposits (already implemented in SavingsAccount)
- A free dollar when you open your account (let multiple inheritance do the job)
```python
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1
# Look up order: Checking Account, SavingsAccount, Account (Subclass first, then baseclass)
```

Be careful with multiple inheritance.

## Q&A
- 00:03​ Is inheritance recommended these days?
  - Inheritance method is fine, inheritance attributes are complicated.
- 01:34​ How do you evaluate b.z.z.z in the video called "Review: Attributes Lookup, Methods, & Inheritance"?
  - To evaluates b.z.z.z, you need to evaluate b.z.z (dot evaluation); b.z.z -> b.z -> b
- 04:50​ How do you evaluate a.z == b.z in the same video?
  - Type Check can directly evaluates this expression.
- 08:21​ How do you refer to attributes of an object that is part of another object when not using inheritance?
  - In composition, you can usually use a chain of dot expression. (Ultimately you need to get a pointer to the object)
- 11:37​ Can Account.deposit(...) be used to invoke a method even when not overriding an existing method?
  - Yes. But overriding is an occasion that you use funtion instead of method as a short hand.
- 13:32​ What is super() and how does it work?
  - let python do 1. Find the parent class 2. Fill the self argument. 
```python
Account.withdraw(self, amount + self.withdraw_fee)
# Alternatively
super().withdraw(amount + self.withdraw_fee)
```
- 17:15​ If a class doesn't have \__init__, can you pass in arguments when you construct an instance?
  - Yes.
- 18:05​ Do you have to call the constructor function \__init__?
  - Constructor is close relative to an instance.
- 19:36​ Why Does AsSeenOnTVAccount use the SavingsAccount deposit instead of the Account deposit?
  - Look up order. Multiple inheritance is what still developing.
- 22:15​ Is the "Review: Attributes Lookup, Methods, & Inheritance" slide representative of what students are supposed to know for the midterm?
- 23:11​ When writing a program, how do you keep track of what is an instance attribute and what's a class attribute?
  - Instance attribute is directly related to the object. You might need use instance attribute to override class attribute when you are working with other's code.
- 24:31​ For Lab 4 Q 5, Maximum Subsequences, how do you understand the solution by tracing through it?
  - Tracing is not what human should do, you should think recursively when you encounter this situation. Debugging should use simplified examples. Want to know environment diagram is fine, but doing it by hand is tough.

# Ch. 2.5
## Interfaces
An object interface is a collection of attributes and conditions on those attributes. In some programming languages such as Java, interface implementations must be explicitly declared. In others such as Python, Ruby, and Go, any object with the appropriate names implements an interface.

## Multiple Inheritance
There is no correct solution to the inheritance ordering problem, as there are cases in which we might prefer to give precedence to certain inherited classes over others. However, any programming language that supports multiple inheritance must select some ordering in a consistent way, so that users of the language can predict the behavior of their programs.

### Further Reading
Python resolves this name using a recursive algorithm called the C3 Method Resolution Ordering. The method resolution order of any class can be queried using the mro method on all classes.
```python
>>> [c.__name__ for c in AsSeenOnTVAccount.mro()]
['AsSeenOnTVAccount', 'CheckingAccount', 'SavingsAccount', 'Account', 'object']
```

## The Role of Objects
Object-oriented programming is particularly well-suited to programs that model systems that have separate but interacting parts. It promotes a *separation of concerns* among the different aspects of the program.

However, Functional abstractions provide a more natural metaphor for representing relationships between inputs and outputs. One should not feel compelled to fit every bit of logic in a program within a class, especially when defining independent functions for manipulating data is more natural. Functions can also enforce a separation of concerns.

Multi-paradigm languages such as Python allow programmers to match organizational paradigms to appropriate problems. Learning to identify when to introduce a new class, as opposed to a new function, in order to simplify or modularize a program, is an important design skill in software engineering that deserves careful attention.