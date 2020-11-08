"""
Given a string ‘str’ of digits, find the length of the longest substring of ‘str’, such that the length of the substring is 2k digits and sum of left k digits is equal to the sum of right k digits.

String len <= 10
H 6 T 2000
Tag str math

In des
First line contains a single string only.

Ot des
Print the length

123123
6

1538023
4
11111
4

2433434
4

1234567891
6

Exp
The complete string is of even length and sum of first and second
half digits is same

Hint
A Simple Solution is to check every substring of even length.

"""
def findLength(str): 

	n = len(str) 
	maxlen = 0 
	for i in range(0, n):  
		for j in range(i+1, n, 2): 
				
					
			length = j - i + 1
			leftsum = 0
			rightsum =0
			for k in range(0,int(length/2)): 
			
				leftsum += (int(str[i+k])-int('0')) 
				rightsum += (int(str[i+k+int(length/2)])-int('0')) 
			if (leftsum == rightsum and maxlen < length): 
					maxlen = length 
		
	
	return maxlen  
str = input()
print(findLength(str)) 

