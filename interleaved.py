"""
Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B. C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.


In des
First line contain three space separated strings.

Ot des
Print yes or no


Exp
The string XXXXZY can be made by 
interleaving XXY and XXZ
String:    XXXXZY
String 1:    XX Y
String 2:  XX  Z

Hint
If the first character of C matches with the first character of A, we move one character ahead in A and C and recursively check.
If the first character of C matches with the first character of B, we move one character ahead in B and C and recursively check.


"""
def isInterleaved(A, B, C): 

	M = len(A) 
	N = len(B)  
	IL = [[False] * (N + 1) for i in range(M + 1)] 

	if ((M + N) != len(C)): 
		return False
	for i in range(0, M + 1): 
		for j in range(0, N + 1): 
			if (i == 0 and j == 0): 
				IL[i][j] = True

			elif (i == 0): 
				if (B[j - 1] == C[j - 1]): 
					IL[i][j] = IL[i][j - 1] 
			elif (j == 0): 
				if (A[i - 1] == C[i - 1]): 
					IL[i][j] = IL[i - 1][j] 
			elif (A[i - 1] == C[i + j - 1] and
				B[j - 1] != C[i + j - 1]): 
				IL[i][j] = IL[i - 1][j] 
			elif (A[i - 1] != C[i + j - 1] and
				B[j - 1] == C[i + j - 1]): 
				IL[i][j] = IL[i][j - 1] 
 
			elif (A[i - 1] == C[i + j - 1] and
				B[j - 1] == C[i + j - 1]): 
				IL[i][j] = (IL[i - 1][j] or IL[i][j - 1]) 
		
	return IL[M][N] 
def test(A, B, C): 

	if (isInterleaved(A, B, C)): 
		print('yes') 
	else: 
		print('no') 

a,b,c=input().split()
if __name__ == '__main__': 
	test(a, b, c) 

