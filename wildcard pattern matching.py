"""
Given two strings 'str' and a wildcard pattern 'pattern' of length N and M respectively,  You have to print '1' if the wildcard pattern is matched with str else print '0' .

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

Note: The matching should cover the entire str (not partial str).
Constraints:
1 <= length of(str,pat) <= 200

H 7
T 2300
Tag yahoo string

In des
First line contain string s.
Second line contain string,denotes the pattern.

Ot des
Print 1 if it is wildcard pattern else 0.

baaabab
ba*a?

1

baaabab
*****ba*****ab

1

baaabab
a*ab

0

water
*r
1


master
m*e

0

Exp
From sample:replace '*' with "aab" and '?' with 'b'.

Hint
Each occurrence of ‘?’ character in wildcard pattern can be replaced with any other character and each occurrence of ‘*’ with a sequence of characters such that the wildcard pattern becomes identical to the input string after replacement.



"""
def strrmatch(strr, pattern, n, m):  
	if (m == 0): 
		return (n == 0) 
	lookup = [[False for i in range(m + 1)] for j in range(n + 1)] 
	lookup[0][0] = True 
	for j in range(1, m + 1): 
		if (pattern[j - 1] == '*'): 
			lookup[0][j] = lookup[0][j - 1] 
	for i in range(1, n + 1): 
		for j in range(1, m + 1): 
			if (pattern[j - 1] == '*'): 
				lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j] 
			elif (pattern[j - 1] == '?' or strr[i - 1] == pattern[j - 1]): 
				lookup[i][j] = lookup[i - 1][j - 1] 
			else: 
				lookup[i][j] = False
	
	return lookup[n][m] 
strr = input()
pattern = input()

if (strrmatch(strr, pattern, len(strr),len(pattern))): 
	print("1") 
else: 
	print("0") 
