"""
hard 6
There are N number of persons in a party, find the total number of handshake
such that a person can handshake only once.

In des
First line contain integer N,denotes number of persons in party

Ot des
Print the count of handshakes

I
3
O
3

I
5
O
10

I
10
O
45

I
20
O
190

I
2
O
2
Explanation
There are 3 possibilities (1,2), (1,3), (2,3).

T 3000
Hint
Find the count of possible pair which shoud not repeated.
"""
 
def handshake(n):
        
	if (n == 0): 
		return 0
	else: 
		return (n - 1) + handshake(n - 1)
	    
	    
                
n = int(input())
print(handshake(n)) 

