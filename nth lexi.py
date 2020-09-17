"""
Given a string of length m containing lowercase alphabets only. We need to find the n-th permutation of string lexicographically.

Tag cisco string
7
2500

3
aba
baa

2
aba
aba

3
abc
bac

6
what
awth

2
at
ta

Exp
All possible permutation in 
sorted order: abc, acb, bac,
bca, cab, cba

Hint
The total number of permutation of a string formed by N characters(all distinct) is N!
The Total number of permutation of a string formed by N characters (where the frequency of character C1 is M1, C2 is M2… and so the frequency of character Ck is Mk) is N!/(M1! * M2! *….Mk!).
The total number of permutation of a string formed by N characters(all distinct) after fixing the first character is (N-1)!

"""
MAX_CHAR = 26
MAX_FACT = 20
fact = [None] * (MAX_FACT) 
def precomputeFactorials(): 

	fact[0] = 1
	for i in range(1, MAX_FACT): 
		fact[i] = fact[i - 1] * i 
def nPermute(string, n): 
	precomputeFactorials() 
	length = len(string) 
	freq = [0] * (MAX_CHAR) 
	for i in range(0, length): 
		freq[ord(string[i]) - ord('a')] += 1
	out = [None] * (MAX_CHAR) 
	Sum, k = 0, 0 
	while Sum != n: 

		Sum = 0
		for i in range(0, MAX_CHAR): 
			if freq[i] == 0: 
				continue 
			freq[i] -= 1 
			xsum = fact[length - 1 - k] 
			for j in range(0, MAX_CHAR): 
				xsum = xsum // fact[freq[j]] 
			Sum += xsum 
			if Sum >= n: 
				out[k] = chr(i + ord('a')) 
				n -= Sum - xsum 
				k += 1
				break
			if Sum < n: 
				freq[i] += 1 
	i = MAX_CHAR-1
	while k < length and i >= 0: 
		if freq[i]: 
			out[k] = chr(i + ord('a')) 
			freq[i] -= 1
			i += 1
			k += 1
		
		i -= 1
	print(''.join(out[:k])) 
n = int(input())
string = input()
nPermute(string, n)
