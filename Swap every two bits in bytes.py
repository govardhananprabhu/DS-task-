"""
Swap all the pair of bits in a byte.
Before swapping: 11-10-11-01
After swapping: 11-01-11-10

H 5
T 1500

Tag cisco bit

In des
First line contains an unsigned integer x.

Ot des
Print the integer after swap

4
8

20
40

2
1

24
4

14
5
Exp
From sample
bin of 4 is 00000100 after swap int of 00001000 is 8

Hint
Swap every two bits in the binary representation of given integer and print the int value of swapped representation.

""" 
import math 
def swapBitsInPair( x): 
	return ((x & 0b10101010) >> 1) or ((x & 0b01010101) << 1)  
x = int(input()) 
print(swapBitsInPair(x)) 
