# Lecture
## Modular Design
### Separation of Concerns
- A design principle: Isolate different parts of a program that address different concerns.
  - Other parts of the programs should know each other as little as possible
- A modular component can be developed and tested independently

### Restaurant Search Engine
> You should not forget how John write the code.
```py
def search(query, ranking=lambda r:-r.star):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)

def reviewed_both(r, s):
    return len([x for x in r.reviewers if x in s.reviewers])

class Restaurant:
    all = []
    def __init__(self, name, stars, reviewers)
        self.name, self.starts = name, stars
        self.reviewers = reviewers
        Restaurant.all.append(self)

    def similiar(self, k, similarity=reviewed_both):
        "Return the K most similar restaurants to SELF."
        others = list(Restaurant.all).remove(self)
        return sorted(others, key= lambda r: -similarity(self,r) )[:k]

    def __repr__(self):
        return '<' + self.name + '>'

import json

reviewers_for_restaurant = {}
for line in open('reviews.json'):
    r = json.loads(line)
    biz = r['business_id']
    if biz not in reviewers_for_restaurant:
        reviewers_for_restaurant[biz] = [r['user_id']]
    else:
        reviewers_for_restaurant[biz].append(r['user_id'])

for line in open('restaurants.json'):
    r = json.loads(line)
    reviewers = reviewers_for_restaurant[r['business_id']]
    Restaurant(r['name'], r['stars'], reviewers)

results = search('Thai')
for r in results:
    #print(r, 'is similiar to', r.similar(3))
    print(r, 'shares reviewers with', r.similar(3))
```

## Set Intersection
```py
def reviewed_both(r, s):
    return len([x for x in r.reviewers if x in s.reviewers])
```
### Linear-Time Intersection of Sorted Lists
This is a quadratic operation. We can keep a sorted list of reviewers:
```python
Restaurant(r['name'], r['stars'], sorted(reviewers))
```
And use a linear-time intersection.
```py
def fast_overlap(s, t):
    i, j, count =0, 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            count, i, j = count+1, i+1, j+1
        elif s[i] < t[j]:
            i += 1
        else:
            j += 1
    return count
```
See [Lecture 21](./Lecture%2021%20Composition.md##Sets) for more about sets in python.

## Q&A
- 00:03​ Fall 2019 Midterm 2 Question 4
  - Check all elements' backward then you meet the forward requirement. max(0, i-k)
- 07:52​ Is there a good way to practice thinking logically?
- 10:30​ Spring 2020 Midterm 2 Question 2(b)
```py
def power(n, k):
    """Yield all powers of k whose digits appear in order in n.
    
    >>> sorted(power(12345, 5))
    [1, 5, 25, 125]
    >>> sorted(power(54321, 5))         # 25 and 125 are not in order
    """
    def build(seed):
        """yield all non-negative intergers whose digits appear in order in seed.
        """
        if seed == 0:
            yield 0
        else:
            for x in build(seed // 10):
                yield x
                yield 10 * x + seed % 10

    yield from filter(curry2(is_power)(k), build(n))
```
- 16:20​ How do you use a built-in set to perform set intersection efficiently?
  - Hashing, which archieves constant time membership test. You learned it in CS61B
- 18:31​ Lab 8 Optional Question 6
- 25:49​ What does super() do in a class that inherits from two different classes?
  - Looking up the attr in the order of inheritance.
- 26:35​ Fall 2018 Midterm 2 Question 6
```py
if i > 0:
    recursive_f(s.rest, t, i-1, j-1)
```