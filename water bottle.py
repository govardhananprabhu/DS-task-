"""
Given two integers N and E, where N represents the number of full water bottles and E represents the number of empty bottles that can be exchanged for a full water bottle. The task is to find the maximum number of water bottles that can be emptied.
H 6 T 2000
Tag math

In des
First line contains 2 integers N,E denotes water bottles of full and empty.

Ot des
Print the count of water bottle can be made empty.
9 3
13

5 4
6

11 10
12

4 2
7

7 5
8

Exp
Empty the 7 fully filled water bottles. Therefore, count = 7
Then exchange 5 bottles to obtain 1 fully filled bottle. Then empty that bottle. 
Therefore, count = 7 + 1 = 8.

Hint
Add the number of bottles that are emptied.
Update after exchanging empty bottles.
Stores the number of bottles left after the exchange.

"""
def maxBottles(n, e): 
	
	s = 0
	b = 0
	a = n 
	while (a != 0): 
		s = s + a  
		a = (a + b) // e 
		b = n - (a * e) 
		n = a + b  
	return s 
 
n,e=map(int,input().split())
s = maxBottles(n, e) 
print(s) 
