# Lecture
## Create Table and Drop Table
```SQL
create table numbers (n, note);
create table numbers (n UNIQUE, note);
create table numbers (n, note DEFAULT "nocomment");
```

## Modifying Tables
For a table t with two columns
- To insert into one column:
```SQL
INSERT INTO t(column) VALUES (value);
```
- To insert into both columns:
```SQL
INSERT INTO t VALUES (value0, value1);
```
- Using update to set new values
```SQL
UPDATE primes SET prime=0 WHERE n>2 and n%2=0;
```
- Using Delete to 
```SQL
DELETE FROM primes WHERE prime=0
```

## DEMO
```SQL
sql> create table primes(n, prime);
sql> drop table if exists primes;
sql> select * from primes;
Error: no such table: primes
sql> create table primes(n UNIQUE, prime DEFAULT 1);
sql> select * from primes;
sql> INSERT INTO primes VALUES (2, 1), (3, 1);
sql> select * from primes;
 n 	 prime 
 2 	 1 
 3 	 1 

sql> INSERT INTO primes(n) VALUES (4), (5), (6), (7);
sql> select * from primes;
 n 	 prime 
 2 	 1 
 3 	 1 
 4 	 1 
 5 	 1 
 6 	 1 
 7 	 1 

sql> INSERT INTO primes(n) SELECT n+6 FROM primes;
sql> select * from primes;
 n 	 prime 
 2 	 1 
 3 	 1 
 4 	 1 
 5 	 1 
 6 	 1 
 7 	 1 
 8 	 1 
 9 	 1 
 10 	 1 
 11 	 1 
 12 	 1 
 13 	 1 

sql> INSERT INTO primes(n) SELECT n+12 FROM primes;

sql> UPDATE primes SET prime=0 WHERE n>2 and n%2=0;
sql> UPDATE primes SET prime=0 WHERE n>3 and n%3=0;
sql> UPDATE primes SET prime=0 WHERE n>5 and n%5=0;
-- sometimes it's easier to build a table by updating 

sql> DELETE FROM primes WHERE prime=0;
sql> select * from primes;
 n 	 prime 
 2 	 1 
 3 	 1 
 5 	 1 
 7 	 1 
 11 	 1 
 13 	 1 
 17 	 1 
 19 	 1 
 23 	 1 
```

## Python and SQL
```py
import sqlite3

db = sqlite3.Connection("n.db") # this will create a n.db in the current location
db.execute("CREATE TABLE nums AS SELECT 2 UNION SELECT 3;")
db.execute("INSERT INTO nums VALUES (?), (?), (?);", range(4, 7))
cursor = db.execute("SELECT * FROM nums;") # this will return a cursor obejct
db.commit() # just like commit in git, store all the change.

>>> print(cursor.fetchall()) # it has a fetchall method to fetch the contents of the result as a list of tuples
[(2,), (3,), (4,), (5,), (6,)]
```

### SQL Injection Attack
Instead use
```py
name = "Robert'); DROP TABLE Students; --"
cmd = "INSERT INTO Students VALUES ('" + name + "');"
db.executescript(cmd)
```
```SQL
INSERT INTO students VALUES ('Robert'); DROP TABLE Students; --');
```
You should use
```py
db.execute("INSERT INTO Students VALUE (?)", [name])
```
```SQL
INSERT INTO Students VALUES ('Robert''); DROP TABLE Students; --');
```

## Database Connections

## Q&A
- 00:03​ What happens if you GROUP BY three different columns?
  - Only rows are same in these three columns will be put into one group
- 02:03​ How does let work?
  - Local variable. Just like lambda function call.
- 05:26​ What happens when you have a lambda with more than one body expression?
  - return the value of the last expression. You do something in the previous expression, but it won't be the return value of the lambda expression.
- 06:34​ Explain the example (lambda (x) a (let ((a x)) a))
- 08:02​ What would happen if a Python program had two connections to a sqlite database?
  - Database is designed to have multiple connections at the same time. You can just do it.
- 09:47​ What happens when you define within a let?
  - Local variable.
- 11:59​ Explain the example (let ((a (define z (+ z 1)))) z)
- 14:32​ What happens if you group by an expression instead of a column name?
```SQL
sql> select n>1, count(*) from numbers;
 n>1 	 count(*) 
 0 	 3 

sql> select n>1 from numbers;       -- count(*) is an aggregation
 n>1 
 0 
 1 
 1 

sql> select n>1, count(*) from numbers group by n>1;
 n>1 	 count(*) 
 0 	 1 
 1 	 2 

sql> select * from numbers;
 n 
 1 
 2 
 3 

```
- 17:51​ How many times does scheme_eval get called in (define (cube a) (* a a a)) (cube 3)?
- 19:25​ What's a recursive select statement?
  - If you found it useful, go fa16 courses. I don't think that worths your time.
- 21:10​ Can you have a SELECT statement within a WHERE clause?
  - If the result of this select is one row & one column table, SQL will treat it as the content of this cell.
- 23:00​ If you had a table of numbers, how would you create a table of primes? (from the exam prep worksheet)