"""
You are given a number N, you have to print the number of integers less than N in the sample space S.

The first line contains an integer N, denoting the number.

Print the count

9

2

36

5

1000000

999

5

1

24

3

From sample:
Numbers are 4 = 1^2 * 2^2, 
9 = 1^2 * 3^2, 
16 = 1^2 * 4^2, 
25 = 1^2 * 5^2, 
36 = 1^2 * 6^2
count =5

Hint
Let us consider a number P = (a2 * b2) such that P <= N. So we have (a2 * b2) <= N. This can be written as (a * b) <= sqrt(N).

So we have to count pairs (a, b) such that (a * b) <= sqrt(N) and a <= b.
Let us take a number Q = (a * b) such that Q <= sqrt(N).

H 4
T 3000 

Tag ola cabs, mathematics,accolite
"""
import math  
def countNumbers(N): 
	return int(math.sqrt(N)) - 1
 
N = int(input())
print(countNumbers(N)) 

