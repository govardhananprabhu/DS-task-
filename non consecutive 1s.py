"""
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.

In des
First line contain integer N,denotes the range

Ot des
Print the count of possible binary representation without consecutive 1.
2
3

3
5


H 5
T 2000
Exp
The 3 strings are 00, 01, 10

Hint
Find the count of binary representation without consecutive 1s for the given range. 

"""
def countStrings(n): 

	a=[0 for i in range(n)] 
	b=[0 for i in range(n)] 
	a[0] = b[0] = 1
	for i in range(1,n): 
		a[i] = a[i-1] + b[i-1] 
		b[i] = a[i-1] 
	
	return a[n-1] + b[n-1] 
N=int(input()) 

print(countStrings(N)) 
