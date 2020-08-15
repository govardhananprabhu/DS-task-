"""
Given a positive integer N, find the maximum number of segments of lengths a, b and c that can be formed from N.

In des
First line contain integer N,denotes the total length.
Second line contain three space separated integers,denotes segments.

Ot des
Print the max possible segments

Exp
17
2 1 3
17

7
5 2 5
N can be divided into 2 segments of lengths
2 and 5.

Hint
From the given segments,find the possibility of N can be divided into segments whose segments sum equals to N.

H-6
T 2000

""" 
def maximumSegments(n, a, b, c) : 

	dp = [-1] * (n + 10) 


	dp[0] = 0


	for i in range(0, n) : 
	
		if (dp[i] != -1) : 
		
			 
			if(i + a <= n ): 	 
				dp[i + a] = max(dp[i] + 1, 
							dp[i + a]) 
							
			if(i + b <= n ): 	 
				dp[i + b] = max(dp[i] + 1, 
							dp[i + b]) 
							
			if(i + c <= n ): 	 
				dp[i + c] = max(dp[i] + 1, 
							dp[i + c]) 

	return dp[n] 


n = int(input())
a,b,c=map(int,input().split())
print (maximumSegments(n, a, b, c)) 

