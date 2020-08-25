"""
Given a positive integer N, print count of set bits in it. For example, if the given number is 6(binary: 110), output should be 2 as there are two set bits in it.

In des
First line contains of integer input N.

Ot des
Print count of set bits in it.

6

2

11

3

13

3

Exp
From sample
Binary representation of 13 is 1101 and has 3 set bits

Hint
Simple Method Loop through all bits in an integer, check if a bit is set and if it is then increment the set bit count.

H 5
T 2000


"""
def countSetBits(n): 
	count = 0
	while (n): 
		count += n & 1
		n >>= 1
	return count 
i = int(input())
print(countSetBits(i)) 


