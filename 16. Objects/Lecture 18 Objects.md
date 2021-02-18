# Lecture
## Classes & Objects
A class combines (and abstracts) data and functions; An object is an instantiation of a class.

Constructor:
- allocate memory for a object
- initializes the object with values
- return the address of the object

## Object-Oriented Programming
- A method for organizing modular programs (every part in the program has its own task)
  - Abstraction barriers
  - Bundlin together information and related behavior
- A metaphor for computation using distributed state
  - Each *object* has its own local state.
  - Each object also knows how to manage its own local state, based on method calls.
  - Method calls are messages passed between objects. (I think it refers to the [dispatch-funciton](./Lecture%2016%20Mutable%20Functions.md#Ch.-2.4), to regard the method after dot as a message, which is a special argument for a function)
  - Several obejcts may all be instances of a common type.
  - Different types may relate to each other.
- Specialized syntax & vocabulary to support this metaphor

## Classes
A class serves as a template for its instances.

### Class Statment
- creat a new class and binds that class to \<name> in the first frame of the current environment.
- assignment & def statements in \<suite> create attributes of the class (not names in frames)

### Object Construction
When a class is called:
- a new instance of that class is created
- the \__init__ method of the class is called with the new object as its first argument (named self), along the additional arguments

## Methods
Methods are defined in the suite of a class statement. They create function objects as always, but their names are bound as attributes of the class.

### Invoking Methods
All invoked methods have access to the object via the *self* parameter, and so they can all access and manipulate *the object's* state.
```python
class Account:
    ...
    def deposit(self, amount):  # defined with two arguments
        self.balance = self.blance + amount
        return self. balance
```
Dot notation automatically supplies the first argument to a method.
```python
>>> tom_account = Account('Tom')
>>> tom_account.deposit(100)    # Invoked with one argument
000
```

### Dot Expression
- Obejct receive messages via dot notation.
- Dot notation accesses attributes of the instance *or* its class.
```
<express>.<name>
```
- The \<expression> can be any valid Python expression.
- The \<name> must be a simple name (not an expression that evaluates to a name)
- Evaluates to the value of the attrivute *looked up* by \<name> in the object that is the value of the \<expression>

## Attributes
### Accessing
```python
>>> getattr(tom_account, 'balance')
10
>>> hasattr(tom_account, 'deposit')
True
```
- getattr and dot expressions look up a name in the same way. It is athe function equivalent of dot natation.
- Looking up an attribute name in an object may return:
  - One of its instance attributes, if there's not:
  - One of the attributes of its class

### Methods and Functions
Python distinguishes between:
- *Functions*
- *Bound methods*, which couple together a function and the obejct on which that method will be invoked.

> Object + Function = Bound Method

```python
>>> type(Account.deposit)
<class 'function'>
>>> type(tom_account.deposit)
<class 'method'>

>>> Account.deposit(tom_account, 1001)
1011
>>> tom_account.deposit(1000)
2011
```

### Looking Up Attributes by Name
    <expression>.<name>

To evaluate a dot expression:
1. Evaluate the \<expression> to the left of the dot, which yields the object of the dot expression.
2. \<name> is matched against the instance attributes of that object; if an attribute with that name exists, its value is returned.
3. If not, \<name> is looked up in the class, which yields a *class attribute value*.
4. That value is returned unless it's a function, in which case a *bound method* is returned instead.

### Class Attributes
Class attributes are "shared" across all instances of a class because they are attributes of the class, not the instance. (it only takes one piece of memory)

## Q&A
- 00:02​ Is a method a class attribute?
  - Yes, but they mostly are called methods
- 01:13​ What's a bound method and how is it used?
  - A method with a *self* argument.
- 04:13​ What can self refer to?
  - An object of the class, which is unknown untill someone pass mannually or using dot expression or. It is a placeholder.
- 05:20​ Can self only be used to refer to attributes, or also to methods?
  - Both, you can use self.\<bound method>.
- 06:31​ Is assigning to attributes using self a form of mutation?
  - Yes, it changes the object.
- 07:35​ In the example where an instance and its class share an attribute name, is there a way to remove the attribute from the instance?
  - del \<instance>.\<attribute> It was used rarely.
- 11:39​ Is there an equivalent in Python to the "public" and "private" keywords in Java?
  - There is a convention that "_" prefix shows this thing is not for user. But just a convention, not enforcement.
- 15:25​ Is there a way to make a user-defined class immutable?
  - No built-in python way.
- 16:55​ Should you use selector functions instead of accessing attributes directly?
  - No perfect general rules. But remember the "_" convention.
- 21:56​ What's the difference between remove and del?
  - del is more general. remove is a class attribute.
- 23:46​ Can you explain Q10 and Q12 from Homework 3? 
- 32:27​ What's a static method and when would you use it?
  - It's a convention (at least in Python, because you will not run into trouble if you don't use @staticmethod) that create normal functions in a class.
- 34:43​ Is there anything you don't like about Python's object system?
  - Minimalism is a double sword. Farid and John said Python is not good for large program.

# Ch. 2.5 Object-Oriented Programming
## Objects and Classes
The act of creating a new object instance is known as *instantiating* the class. The attributes specific to a particular object, as opposed to all objects of a class, are called *instance attributes*. In the broader programming community, instance attributes may also be called *fields*, *properties*, or *instance variables*.

Functions that operate on the object or perform object-specific computations are called methods. Methods are *invoked* on a particular object.

## Defining Classes
When a class statement is executed, a new class is created and bound to \<name> in the first frame of the current environment. The suite is then executed.

New objects that have user-defined classes are only created when a class (such as Account) is instantiated with *call expression syntax*.

When a method is invoked via dot notation, the object itself plays a dual role:
- First, it determines what the name *withdraw* means; *withdraw* is not a name in the environment, but instead a name that is local to the *Account* class. 
- Second, it is bound to the first parameter *self* when the *withdraw* method is invoked.

## Message Passing and Dot Expressions
Methods and instance attributes are the fundamental elements of OOP. The two concepts replicate the behavior of a dispatch dictionary in a message passing implementation of a data value.
- Objects take messages using dot notation.
- Objects also have named local state values (the instance attributes).
- Named local state values don't need *nonlocal* statement to implement.

Dot notation is a syntactic feature of Python that formalizes the message passing metaphor. The language syntax allows us to use the message name directly like a expression.

### Methods and Functions
To achieve automatic self binding, Python distinguishes between *functions* and *bound methods*. A bound method value is already associated with the *self* argument.
```python
>>> type(Account.deposit)       # A standard two-argument function with parameters self and amount.
<class 'function'>
>>> type(spock_account.deposit) # The name self will be bound to spock_account automatically when the method is called.
<class 'method'>                # We can sese the difference. It is the same when we use the getattr function
```

### Name Conventions
- Class names are conventionally written using the CapWords(CamelCase) convention.
- Method names follow the standard convention of naming functions using lowercased words separated by underscores.
- "_" prefix shows that They are not part of the abstraction defined by a class.
  - They are part of the implementation.
  - Should only accessed within methods of the class itself.
  - Should not be touched by users