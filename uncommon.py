"""
Two strings are given and you have to modify 1st string such that all the common characters of the 2nd strings have to be removed and the uncommon characters of the 2nd string have to be concatenated with uncommon characters of the 1st string.
string len <= 10
H 5 T 2000
Tag string

In des
First line contains 2 string only.

ot des
Print the uncommon character without any space.

aacdb gafd

cbgf

abcs cxzca

bsxz

water retae

w

master guvi
masterguvi

guvi geek
uvieek

Exp
From sample the uncommon characters are cbgf

Hint
The idea is to use hash map where key is character and value is number of strings in which character is present. If a character is present in one string, then count is 1, else if character is present in both strings, count is 2.

"""
def concatenetedString(s1, s2): 
	res = ""
	m = {} 
	for i in range(0, len(s2)): 
		m[s2[i]] = 1
	for i in range(0, len(s1)): 
		if(not s1[i] in m): 
			res = res + s1[i] 
		else: 
			m[s1[i]] = 2		 
	for i in range(0, len(s2)): 
		if(m[s2[i]] == 1): 
			res = res + s2[i] 

	return res	 
s1,s2 = input().split()
print(concatenetedString(s1, s2)) 

 
