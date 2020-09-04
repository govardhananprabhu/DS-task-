"""
Given a number N and a bit number K, check if Kth bit of N is set or not. A bit is called set if it is 1. Position of set bit '1' should be indexed starting with 0 from RSB side in binary representation of the number.
H 4
T 1000

Tag cisco bit

In des
The first line contain an integer N.
The second line contains an integer  K.

Ot des
Print "yes" (without quotes) if Kth  bit is set else print "no" (without quotes).

5
1
yes

2
3
no

33
2
no

33
1
yes

64
7
yes


Exp
From sample:
5 is represented as 101 in binary and has its first bit set.

Hint
Left shift given number 1 by k-1 to create a number that has only set bit as k-th bit.If bitwise AND of n and temp is non-zero, then result is yes else result is no.
"""
def isKthBitSet(n, k): 
	if n & (1 << (k - 1)): 
		print( "yes") 
	else: 
		print("no")  
n = int(input())
k = int(input())
isKthBitSet(n, k)  
