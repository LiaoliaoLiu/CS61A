# Lecture
## Declarative Programming
> Database Management System

In **decelarative languages** such as SQL & Prolog:
- A "program" is a description of the desired result
- The interpreter figures out how to generate the result

In **imperative languages** such as Python & Scheme:
- A "program" is a descrption of computational processes
- The interpreter carries out execution/evaluation rules

## Structured Query Lanuage (SQL)
The SQL language is an ANSI and ISO standard, but DBMS's implement custom variants.
- A *select* statement creates a new table, either from scratch or by projecting a table.
- A *create table* statement gives a global name to a table
- Lots of other statements exist: *analyze, delete, explain, insert, replace, update,* etc.
- Most of the important action is in the *select* statement
- The code for executing *select* statements fits on a single sheet of paper

### Selecting Value Literals & Naming Tables
- A *select* statement always includes a comma-separated list of column descriptions
- A column description is an expression, optionally followed by *as* and a column name
```SQL
select [expression] as [name], [expression] as [name];
```
- Selecting literals creates a one-row table
- The union of two select statements is a table containing the rows of both of their results
- SQL is often used as an interactive language
- The result of a *select* statement is displayed to the user, but not stored
- A *create table* statement gives the result a name
```SQL
create table [name] as [select statement];
```
```SQL
create table parents as
    select "delano" as parent, "herbert" as child union
    select "abraham" , "barack" union
    select "abraham" , "clinton" union
    select "fillmore" , "abraham" union
    select "fillmore" , "delano" union
    select "fillmore" , "grover" union
    select "eisenhower" , "fillmore";

```

### Select Statements Projecting  Existing Tables
- A *select* statement can specify an input table using a *from* clause
- A subset of the rows of the input table can be selected using a *where* clause
- An ordering over the remaining rows can be declared using an *order by* clause
- Column descriptions determine how each input row is projected to a result row
```SQL
select [columns] from [table] where [condition] order by [order];
```
```SQL
sql> select parent from parents where parent > child;
 parent 
 fillmore 
 fillmore 
```

### Arithmetic in Select Expressions
- In a select expression, column names evaluate to row values
- Arithmetic expressions can combine row values and constants
```SQL
create table lift as
select 101 as chair, 2 as single, 2 as couple union
select 102 , 0 , 3 union
select 103 , 4 , 1;

sql> select chair, single + 2 * couple as total from lift;
 chair 	 total 
 101 	 6 
 102 	 6 
 103 	 6 
```

## Q&A
- 00:04​ Can you convert a two-argument procedure to a one-argument procedure with a lambda expression?
  - eval_env = lambda first: scheme_eval(first, env)
- 01:24​ What does validate_procedure do in the Scheme project?
  - To make sure the argument is a validate Scheme procedure
- 01:52​ Is the datascience module from Data 8 using SQL for its implementation?
- 03:28​ If the arguments you want to pass to a procedure are in a list, how do you pass them all?
  - built-in procedure *apply*. It just
```scheme
scm> (define values '(1 2))
values
scm> (+ values)
Traceback (most recent call last):
 0	(+ values)
Error: operand 0 ((1 2)) is not a number
scm> (apply + values)
3
```
- 04:55​ What do "linear" and "quadratic" mean when describing how long something takes?
- 07:55​ What is NoSQL and how is it related to SQL?
  - Variant. NoSQL databases oftentimes still use sth that allmost exactly like SQL in order to access them. It increase the performance at synchronization issue's cost. SQL is slow in a large size.
- 11:50​ Is SQL a fast language or is it slow?
  - It is fast in a way that:
    - You don't need to pay attention to the time cost of operations, the database engine does it for you.
  - It is slow in three ways that:
    - You are doing tons of arithmetics in the SQL query.
    - Many computers are trying to accessing the same database at once. Some have to wait other until they finish.
    - You don't set up the database right.
- 14:58​ Why are keywords all caps in SQL, and how come they aren't in 61A examples?
  - Maybe it's good convention for the past.
- 17:33​ Can you create an empty row and fill it in later?
  - It's possible, but I forgot how to create a empty.
- 23:06​ Can a program not written in SQL use SQL to store data internally?
  - Python has a built-in SQLite interface.
- 24:45​ What are the constraints on the values that can be in a SQL column?
  - SQLite lets you do it like Python, but most other DBMS are more like C.
- 27:04​ Can you create a SQL table by starting with an empty grid and then filling it in?
  - It's more often to create a table with no row but particular set of columns of their names.
- 28:12​ Can you work alone on Scheme and are there checkpoints for the challenge version?
- 29:09​ Can you have a value in a SQL database that is changing over time?
  - No, it must be static. But you can use other programs to change it. It's more often that you have a table that each row is different versions of the same thing. You have a column what version it is. And you can store things like age by their born time.

# Ch. 4.3 Declarative Programming
In addition to streams, data values are often stored in large repositories called databases.
- Each value stored in a database is called a *record*.
- Records are retrieved and transformed using *queries*, which are statements in a query language.
- Statements do not describe computations directly, but instead describe the desired result of some computation.
  - *query interpreter* produces such a result
> A declarative language abstracts away procedural details, instead focusing on the form of the result.

## Select Statements
It is often helpful to give each column a name. Columns automatically use their expression as default.
```SQL
create table cities as
   select 38 as latitude, 122 as longitude, "Berkeley" as name union
   select 42,             71,               "Cambridge"        union
   select 45,             93,               "Minneapolis";

sql> select name, 60*abs(latitude-38) from cities;
 name 	 60*abs(latitude-38) 
 Berkeley 	 0 
 Cambridge 	 240 
 Minneapolis 	 420

sql> select name, 60*abs(latitude-38) as distance from cities;
 name 	 distance 
 Berkeley 	 0 
 Cambridge 	 240 
 Minneapolis 	 420 
```