# Lecture
## Two's Complement
1. Start with an unsigned 4-bit binary number where left-most bit is 0
   - 0110 = 6
2. Complement your binary number (flip bits)
   - 1001

3. add one to your binary number
   - 1010 = 06 (This presentation is not for humans but computers)

| Postive | Complement |  +1   | Negative |
| :-----: | :--------: | :---: | :------: |
|   000   |    111     |  000  |    0     |
|   001   |    110     |  111  |    -1    |
|   010   |    101     |  110  |    -2    |
|   011   |    100     |  101  |    -3    |
|  100?   |    011     |  100  |    -4    |

You see the pattern. "100" is -4. range is $[-2^{n-1}, 2^{n-1}-1$

## Q&A
### What does it mean for a computer to be 64-bit
How large of an integre a computer can represent, like color depth in picture.

### Base 10 computer
There is not obivious advantage. John said if this happened, computers don't have to do the conversion to ten. But this kind of operation only takes up a small amount of computations in total. And hardware will be more complex, as there will be more basic circuit. And arithmetic rules in base 2 is trivial, while in ten is not.

### Key in Min Function
You can use it to find the closest to a value.
```python
>>> min([3,2,5,6], key = lambda x:abs(x*x-24))
5
```

# Lab05
## Using Doctest to Check Abstraction Type
See lab05 function check_city_abstraction