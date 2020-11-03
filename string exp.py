"""
Given a string consisting of only 0, 1, A, B, C where
A = AND
B = OR
C = XOR
Calculate the value of the string assuming no order of precedence and evaluation is done from left to right.

Constraints – The length of string will be odd and less than 10. It will always be a valid string.
Example, 1AA0 will not be given as an input.

H 5 T 1000
Tag string bit

In des
First line contains only one string.

Ot des
Print the result after expression

1A0B1
1

1C1B1B0A0
0

1C1B1B
18

1AB2
2

123A2C
19

Exp
1 AND 0 OR 1 = 1

Hint
The idea is to traverse all operands by jumping a character after every iteration. For current operand str[i], check values of str[i+1] and str[i+2], accordingly decide the value of current subexpression.

""" 
import math as mt 

def evaluateBoolExpr(s): 

	n = len(s)  
	for i in range(0, n - 2, 2): 
		if (s[i + 1] == "A"): 

			if (s[i + 2] == "0" or s[i] == "0"): 
				s[i + 2] = "0"
			else: 
				s[i + 2] = "1"
		elif (s[i + 1] == "B"): 
			if (s[i + 2] == "1" or s[i] == "1"): 
				s[i + 2] = "1"
			else: 
				s[i + 2] = "0"
		else: 
			if (s[i + 2] == s[i]): 
				s[i + 2] = "0"
			else: 
				s[i + 2] = "1"

	return ord(s[n - 1]) - ord("0")  
s = input()
string=[s[i] for i in range(len(s))] 
print(evaluateBoolExpr(string)) 
