"""
Given an integer N, the task is to find the sum of N and it’s maximum prime factor.
2000
cisco mathematics
6

19

38

8

10

4

6

35

42

41

82
Exp
Maximum prime factor of 19 is 19.
Hence, 19 + 19 = 38

Hint
Find the largest prime factor of the number and store it in maxPrimeFact then print the value of N + maxPrimeFact.
"""
from math import sqrt 
def maxPrimeFactors(n): 
	num = n 
	maxPrime = -1; 

	while (n % 2 == 0): 
		maxPrime = 2
		n = n / 2 
	p = int(sqrt(n) + 1) 
	for i in range(3, p, 2): 
		while (n % i == 0): 
			maxPrime = i 
			n = n / i 
	if (n > 2): 
		maxPrime = n 
	sum = maxPrime + num 
	return sum
 
n = int(input())
print(int(maxPrimeFactors(n))) 
