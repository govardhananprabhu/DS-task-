"""
Given a string s, find length of the longest prefix which is also suffix. The prefix and suffix should not overlap.

In des
First line contain string S.

Ot des
Print the count

aabcdaabc
4

Exp
From sample
The string "aabc" is the longest
prefix which is also suffix.

Hint
Since overlapping of prefix and suffix is not allowed, we break the string from middle and start matching left and right string. If they are equal return size of any one string else try for shorter lengths on both sides.

H 7
T 3000

"""
def longestPrefixSuffix(s) : 
	n = len(s) 
	
	for res in range(n // 2, 0, -1) :  
		prefix = s[0: res] 
		suffix = s[n - res: n] 
		
		if (prefix == suffix) : 
			return res 

	return 0	
s = input()
print(longestPrefixSuffix(s)) 
