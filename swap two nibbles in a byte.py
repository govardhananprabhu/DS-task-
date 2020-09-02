"""
Given a byte, swap the two nibbles in it.

First line contains integer N, denotes the byte value.

print the result after swapping the nibbles.



100

70

30
225

120
135

70
100

225
30

For example 100 is be represented as 01100100 in a byte (or 8 bits). The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.

Hint
The expression “x & 0x0F” gives us last 4 bits of x.
The expression “x & 0xF0” gives us first four bits of x.combine them to find decimal value.

H 6
T 1000

Accolite bitwise
"""
def swapNibbles(x): 
	return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 )  

x = int(input())
print(swapNibbles(x)) 
 
