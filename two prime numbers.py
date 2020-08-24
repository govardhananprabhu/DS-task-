"""
Given an even number (greater than 2 ), print two prime numbers whose sum will be equal to given number. There may be several combinations possible. Print only first such pair.


In des
First line contain N integer,denotes the range.

Ot des
Print the two numbers.

74
3 71

1024
3 1021

66
5 61

9990
17 9973

Exp
From sample
3 and 71 are the 2 numbers who's sum is 74.

H 6
T 3000

Hint
The idea is to find all the primes less than or equal to the given number N.Once we have an array that tells all primes, we can traverse through this array to find pair with given sum.

""" 
def SieveOfEratosthenes(n, isPrime): 
	isPrime[0] = isPrime[1] = False
	for i in range(2, n+1): 
		isPrime[i] = True

	p = 2
	while(p*p <= n): 
		if (isPrime[p] == True): 
			i = p*p 
			while(i <= n): 
				isPrime[i] = False
				i += p 
		p += 1
def findPrimePair(n): 
	isPrime = [0] * (n+1) 
	SieveOfEratosthenes(n, isPrime) 
	for i in range(0, n): 
	
		if (isPrime[i] and isPrime[n - i]): 
		
			print(i,(n - i)) 
			return
n = int(input())
findPrimePair(n) 

