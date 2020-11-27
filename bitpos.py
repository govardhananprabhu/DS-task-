"""
Given a number having only one ‘1’ and all other ’0’s in its binary representation, find position of the only set bit.

H 4 T 2000
Tag bit

In des
First line contains only single integer.

Ot des
Print the position

16
5

12
Invalid number

128
8

53
Invalid number

11
Invalid number

Exp
The bit value of 16 is 10000 1 present at 5th position

Hint
The idea is to start from the rightmost bit and one by one check value of every bit.
""" 
def isPowerOfTwo(n): 
	return (True if(n > 0 and
				((n & (n - 1)) > 0)) 
				else False); 
def findPosition(n): 
	if (isPowerOfTwo(n) == True): 
		return -1; 

	i = 1; 
	pos = 1; 
	while ((i & n) == 0):  
		i = i << 1;  
		pos += 1; 

	return pos; 
n = int(input()) 
pos = findPosition(n); 
if (pos == -1): 
	print("Invalid number"); 
else: 
	print(pos); 
