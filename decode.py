"""
Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.

In des
First line contain integer N,denotes the value to be decoded

Ot des
Print the possible decode's count.

121
3

1234
3

Exp
From sample
The possible decodings are "ABA", "AU", "LA"

T 2000
H 6 
 

"""
def numDecodings(s: str) -> int: 
	return numDecodingsHelper(s,len(s)); 

def numDecodingsHelper(s:str, n:int) -> int: 
	if n == 0 or n == 1 : 
		return 1
	count = 0
	if s[n-1] > "0": 
		count = numDecodingsHelper(s,n-1) 
	if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) : 
		count += numDecodingsHelper(s, n - 2) 
	return count 
		 
digits = input()
print(numDecodings(digits)) 
