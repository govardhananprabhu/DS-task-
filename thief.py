"""
There are n houses build in a line, each of which contains some value in it. A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because the owner of the stolen houses will tell his two neighbours left and right side. What is the maximum stolen value?

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes houses values in array.

Ot des
Print the max amount stolen.

7
6 7 1 3 8 2 4
19

5
5 3 4 11 2
16
Exp
From sample
The thief will steal 6, 1, 8 and 4 from the house.

Hint
Find the maximum sum subsequence where no two selected elements are adjacent.

H-5
T-1500


"""
def maximize_loot(hval, n): 
	if n == 0: 
		return 0
	if n == 1: 
		return hval[0] 
	if n == 2: 
		return max(hval[0], hval[1]) 
	dp = [0]*n 
 
	dp[0] = hval[0] 
	dp[1] = max(hval[0], hval[1])  
	for i in range(2, n): 
		dp[i] = max(hval[i]+dp[i-2], dp[i-1]) 

	return dp[-1] 

def main(): 

	N=int(input())
	hval = list(map(int,input().split())) 
	n = len(hval) 
	print(format(maximize_loot(hval, n))) 

if __name__ == '__main__': 
	main() 
