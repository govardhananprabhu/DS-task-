"""
Question
Your class teacher has a list of strings,they have prefix similarities,you
are the class rep help teacher to find the longest common prefix.

Input description
First line has list of strings

Output description
print the Longest common prefix

Explanation
Input: {"apple", "ape", "april"}
smallest string is ape
the longest common string is ap.

Input
apple ape april
Output
ap

Input
go gost gone goosebumps godzilla
Output
go

Input
master mass massive
Output
mas

Input
hello
Output
hello

Input
t t t t
Output
t

Hint
The idea is to sort the array of strings and find the common prefix of the first
and last string of the sorted array.
Solution:"""
def longestCommonPrefix( a): 
	
	size = len(a)  
	if (size == 0): 
		return "" 

	if (size == 1): 
		return a[0] 
	a.sort()
	end = min(len(a[0]), len(a[size - 1]))
	i = 0
	while (i < end and
		a[0][i] == a[size - 1][i]): 
		i += 1

	pre = a[0][0: i] 
	return pre 


if __name__ == "__main__": 

	input = input().split()
	print(longestCommonPrefix(input)) 

 
