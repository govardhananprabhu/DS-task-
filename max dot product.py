"""
Given two arrays of positive integers of size m and n where m > n. We need to maximize the dot product by inserting zeros in the second array but we cannot disturb the order of elements.

In des
First line contain two space separated integers M,N,denotes arrays size.
Second line contain M space separated integrs,denotes arr1 elements.
Third line contain N space separated integrs,denotes arr2 elements.

Ot des
Print the max dot product
5 3
2 3 1 7 8
3 6 7

107

6 3
1 2 3 6 1 4
4 5 1

46
Exp
From sample
We get maximum dot product after
inserting 0 at first and third positions in 
second array.
Maximum Dot Product : = A[i] * B[j] 
2*0 + 3*3 + 1*0 + 7*6 + 8*7 = 107

Hint
We multiply A[i] and B[j] and add to product (We include A[i]).
We exclude A[i] from product (In other words, we insert 0 at current position in B[])
H-5
T-2000
"""
def MaxDotProduct(A, B, m, n): 
	dp = [[0 for i in range(m + 1)] 
			for j in range(n + 1)] 
	for i in range(1, n + 1, 1):  
		for j in range(i, m + 1, 1): 
			
			dp[i][j] = max((dp[i - 1][j - 1] +(A[j - 1] * B[i - 1])) , dp[i][j - 1]) 
 
	return dp[n][m] 

M,N=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
 
print(MaxDotProduct(A, B, M, N)) 

