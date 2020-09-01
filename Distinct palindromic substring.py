"""
Given a string of lowercase ASCII characters, find all distinct continuous palindromic sub-strings of it.

In des
First line contains string S

Ot des
Print the count of distinct continuous palindromic sub-strings of it.

abaaa

5

geek
4

abc
3

hoh
3

noon
4

Exp
From sample
Below are 5 palindrome sub-strings
a, aa, aaa, aba, b

Hint
Find all possible distinct pairs, and print the count of palindrome pairs.

H 6
T 2500

Ola cabs,string 


"""
def palindromeSubStrs(s): 
	m = dict() 
	n = len(s) 
	R = [[0 for x in range(n+1)] for x in range(2)] 
	s = "@" + s + "#"

	for j in range(2): 
		rp = 0 
		R[j][0] = 0

		i = 1
		while i <= n: 
			while s[i - rp - 1] == s[i + j + rp]: 
				rp += 1 
			R[j][i] = rp 
			k = 1
			while (R[j][i - k] != rp - k) and (k < rp): 
				R[j][i+k] = min(R[j][i-k], rp - k) 
				k += 1
			rp = max(rp - k, 0) 
			i += k 
	s = s[1:len(s)-1] 
	m[s[0]] = 1
	for i in range(1,n): 
		for j in range(2): 
			for rp in range(R[j][i],0,-1): 
				m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
		m[s[i]] = 1
	
	print(len(m))
s=input()
palindromeSubStrs(s)
