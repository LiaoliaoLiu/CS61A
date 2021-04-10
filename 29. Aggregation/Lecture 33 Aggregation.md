# Lecture
## Aggregate Functions
An aggregate function in the \[columns] clause computes a value from a group of rows.
```SQL
create table animals as
    select "dog" as kind, 4 as legs, 20 as weight union
    select "cat" , 4 , 10 union
    select "ferret" , 4 , 10 union
    select "parrot" , 2 , 6 union
    select "penguin" , 2 , 10 union
    select "t-rex" , 2 , 12000;

sql> select max(legs) from animals;
 max(legs) 
 4 

sql> select max(legs - weight) from animals
 max(legs - weight) 
 -4 

sql> select avg(legs) from animals;
 avg(legs) 
 3 

sql> select count(legs) from animals;
 count(legs) 
 6 

sql> select count(distinct legs) from animals;
 count(distinct legs) 
 2 
```

An aggregate function also selects a row in the table, which *may be* meaningful.
```SQL
sql> select max(weight), kind from animals;
 max(weight) 	 kind 
 12000 	 t-rex 

sql> select avg(weight), kind from animals; -- This row doesn't exist.
 avg(weight) 	 kind 
 2009.3333333333333 	 cat 
```

## Grouping Rows
Rows in a table can be grouped, and aggregation is performed on each group.

The number of groups is the number of unique values of an expression.
```SQL
sql> select legs from animals group by legs;
 legs 
 2 
 4 

sql> select legs, count(*) from animals group by legs;
 legs 	 count(*) 
 2 	 3 
 4 	 3 

sql> select legs, max(weight) from animals group by legs;
 legs 	 max(weight) 
 2 	 12000 
 4 	 20 

sql> select legs, weight from animals group by legs, weight;
 legs 	 weight 
 2 	 6 
 2 	 10
 2 	 12000 
 4 	 10         -- ferret and cat
 4 	 20 

sql> select max(kind), weight/legs from animals group by weight/legs;
 max(kind) 	 weight/legs 
 ferret 	 2  -- int division by default if two are integer
 parrot 	 3 
 penguin 	 5 
 t-rex 	 6000
```

A having clause filters the set of groups that are aggregated.
```SQL
sql> select weight/legs, count(*) from animals group by weight/legs having count(*)>1;
 weight/legs 	 count(*) 
 2 	 2 
 5 	 2 
```
> The WHERE clause filters out rows, the HAVING clause fillters out entire groups.

Aggregation functions in having clause also will select a row.
```SQL
SELECT name, store from products, lowest_prices where name = item group by category having min(MSRP/rating);S
```

## Q&A
- 01:34​ When selecting a maximum row in the case of a tie, which gets selected?
  - It depends on the underlying implementation. But you can write a longer query to get more control. You should not relay largely on the shortcut.
- 04:19​ When do you use list vs cons in a recursive case?
  - If you don't know how long you are building, you use cons. cons adds one element at a time.
- 07:12​ CS Mentors worksheet 13 Scheme Question 1 (Page 4)
```scheme
(define (skip-list s f)
    (cond   ((null? s) nil)
            ((list? (car s)) (append (skip-list (car s) f) (skip-list (cdr s) f)))
            ((f (car s)) (cons (car s) (skip-list (cdr s))))
            (else (skip-list (cdr s) f))))

; Remember what you have left to process would be easier if you let the interpreter do for you.
```
- 22:14​ Fall 2017 Final Question 6
  - Using recursion to simplify nested if structures.