"""
Given a value T, if we want to make change for T cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

In des
First line contain integer T,denote the total.
Second line contain integer N,size of array which has cents.
Third line contain N space separated integers,denotes cents.

Ot des
Print the possibles

Exp
4
3
1 2 3
4
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4

Hin
Find the count of possible sums with cents in arr equals to T.
H-6
T-2000

3
2
1 3
2


5
4
1 3 2 4
5

1
1
1
1

3
2
1 2
3
"""

def count(S, m, n ): 
	if (n == 0): 
		return 1
	if (n < 0): 
		return 0;  
	if (m <=0 and n >= 1): 
		return 0
	return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 
T=int(input())
N=int(input())
arr = list(map(int,input().split()))
m = len(arr) 
print(count(arr, m, 4)) 

