# Lecture
## Joining Tables
Two tables A & B are joined by a comma to yield *all combos* (n*n) of a row from A & a row from B
```SQL
> sql -init dogs.sql

sql> select * from parents, dogs;
 parent 	 child 	 name 	 fur 
 abraham 	 barack 	 abraham 	 long 
 abraham 	 barack 	 barack 	 short 
 abraham 	 barack 	 clinton 	 long 
 abraham 	 barack 	 delano 	 long 
 abraham 	 barack 	 eisenhower 	 short 
 abraham 	 barack 	 fillmore 	 curly 
 abraham 	 barack 	 grover 	 short 
 abraham 	 barack 	 herbert 	 curly 
...

sql> select * from parents, dogs where child=name;
 parent 	 child 	 name 	 fur 
 abraham 	 barack 	 barack 	 short 
 abraham 	 clinton 	 clinton 	 long 
 delano 	 herbert 	 herbert 	 curly 
 eisenhower 	 fillmore 	 fillmore 	 curly 
 fillmore 	 abraham 	 abraham 	 long 
 fillmore 	 delano 	 delano 	 long 
 fillmore 	 grover 	 grover 	 short 

sql> select * from parents, dogs where child=name and fur='curly';
 parent 	 child 	 name 	 fur 
 eisenhower 	 fillmore 	 fillmore 	 curly 
 delano 	 herbert 	 herbert 	 curly 

sql> select parent from parents, dogs where child=name and fur='curly';
 parent 
 eisenhower 
 delano 
```

## Aliases and Dot Expressions
### Joining a Table with Itself
Two tables may share a column name; dot expressions and aliases disambiguate column values
```SQL
select [columns] from [table] where [condition] order by [order];
```
\[table] is a comma-separated list of table names with optional aliases.

Select all pairs of siblings
```SQL
select a.child as first, b.child as second
    from parents as a, parents as b
    where a.parent = b.parent and a.child < b.child;

 first 	 second 
 barack 	 clinton 
 abraham 	 delano 
 abraham 	 grover 
 delano 	 grover 
```

### Joining Multiple Tables
Multiple tables can be joined to yield all combinations of rows from each
```SQL
create table grandparents as
    select a.parent as grandog, b.child as granpup
    from parents as a, parents as b
    where a.child = b.parent;
```
Select all grandparents with the same fur as their grandchilren
```SQL
select grandog from grandparents, dogs as c, dogs as d
    where grandog = c.name and granpup = d.name and c.fur = d.fur;
```

## Numerical Expressions
Expressions can contain function calls and arithmetic operators.
- Combine values: +, -, *, /, %, and , or
- Transform values: abs, round, not, -
- Compare values: <, <=, >, >=, <>, !=, =

## String Expressions
- String values can be combined to form longer strings (maybe fine)
```SQL
sql> SELECT "hello," || " world";
 "hello," || " world" 
 hello, world 
```
- Basic string manipulation is built into SQL, but differs from Python (mostly you shuold be aware)
```SQL
sql> CREATE TABLE phrase AS SELECT "hello, world" AS s;
sql> SELECT substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) FROM phrase;
 substr(s, 4, 2) || substr(s, instr(s, " ")+1, 1) 
 low 

substr(str, first indx(begin from 1), last)
instr(str, character)
```
- Strings can be used to represent structured values, but doing so is rarely a good idea. (never do this)

## Q&A
- 00:03​ Is SQL pronounced "sequel" or "SQL"?
- 00:44​ Is it common to represent trees using a SQL table?
  - It's more about way of representation not actual data structure.
- 01:42​ What does "dynamic scope" mean?
  - Functions' environments inheriate from where the function is called.
- 03:51​ How many times is eval called when evaluating a Scheme expression?
- 08:46​ How many times is apply called when evaluating a Scheme expression?
- 11:35​ What should and shouldn't you do with strings in SQL?
  - Usually you should use other string manipulation programs
  - Don't use string to represent other data structure