"""
Euler Totient Function (ETF) Φ(n) for an input n is count of numbers in {1, 2, 3, …, n} that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.
H 6
T 2000

Tag cisco, mathematics
In des
First line contains an integer N

Ot des
Print count of Gcd with n is 1

4
2

5
4

6
2

10
4

16
8

Exp
from sample:
gcd(1, 4) is 1 and gcd(3, 4) is 1

Hint
A simple solution is to iterate through all numbers from 1 to n and count numbers with gcd with n as 1.


"""
import math
n = int(input())
c=0
for j in range(1,n+1):
    if math.gcd(j,n)==1:
        c+=1
print(c)
