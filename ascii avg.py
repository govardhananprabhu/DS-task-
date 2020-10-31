"""
Given a string, the task is to find the average of ASCII values of characters in the string.
string len <=10
H 4 T 1000
Tag string math


In des

First line contains only sting.

Ot des
print the avg of ascii value.

for
109

guvi
110

codekatta
104

zen
111

python
112

Exp
'f'= 102, 'o' = 111, 'r' = 114
(102 + 111 + 114)/3 = 109 

Hint
Start iterating through characters of the string and add their ASCII value to a variable. Finally, divide this sum of ASCII values of characters with the length of string , total number of characters in the string.

"""
def averageValue(s): 
	sum_char = 0
	for i in range(len(s)): 
		sum_char += ord(s[i]) 
	return sum_char // len(s) 
s=input()
print(averageValue(s)) 

