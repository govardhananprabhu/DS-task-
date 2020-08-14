"""
Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.
H 4
1000
in des
First line contain integer a.
Second line contain integer b.

ot des
Print the count of bits flipped.

Sample
10
20
4
Exp
From sample
Binary representation of a is 000"0101"0
Binary representation of b is 000"1010"0
We need to flip highlighted four bits in a
to make it b.

Hin
Calculate the XOR of A and B then count the set bits in A XOR B

7
10
3

17
23
2

6
2
1

1
2
2


2
3
1

"""
 
def countSetBits( n ): 
	count = 0
	while n: 
		count += 1
		n &= (n-1) 
	return count 
	

def FlippedCount(a , b): 

	return countSetBits(a^b) 
 
a = int(input())
b = int(input())
print(FlippedCount(a, b)) 


