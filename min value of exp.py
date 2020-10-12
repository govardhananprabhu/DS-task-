"""
Given an algebraic expression of the form (x1 + x2 + x3 + . . . + xn) * (y1 + y2 + . . . + ym) and
(n + m) integers. Find minimum value of the expression using the given
integers.
Consstraint :
n <= 50
m <= 50
-50 <= x1, x2, .. xn <= 50

H 6
T 2000
Tag cisco mathematics

In des
First line contains 2 space separated integers n,m, denotes the count of integers.
Second line contains n+m space separated integers.

Ot des
Print the min value

2 2
1 2 3 4
21

3 1
1 2 3 4
9

5 4
1 3 2 5 4 88 12 21 11
1370

1 1
11 10
110

3 3
1 4 22 1 33 2
236

Exp
From sample:
The expression is (x1 + x2) * (y1 + y2) and
the given integers are 1, 2, 3 and 4. Then
minimum value is (4 + 3) * (2 + 1) = 21.
Hint
A simple solution is to consider all possible combinations of n numbers and remaining m numbers and calculating their values, from which minimum value can be derived.

"""
def minValues(arr, n, m) :	  
	sum = 0
	INF = 1000000000
	MAX = 50
	for i in range(0, (n + m)) : 
		sum += arr[i] 
		arr[i] += 50
	dp = [[0 for x in range(MAX * MAX + 1)] 
				for y in range( MAX + 1)] 
	
	dp[0][0] = 1 
	for i in range(0, (n + m)) : 
		for k in range(min(n, i + 1), 0, -1) : 
			for j in range(0, MAX * MAX + 1) : 
				if (dp[k - 1][j]) : 
					dp[k][j + arr[i]] = 1
	min_value = INF 

	for i in range(0, MAX * MAX + 1) : 
		if (dp[n][i]) : 
			temp = i - 50 * n  									
			min_value = min(min_value, temp * (sum - temp)) 
	print(min_value)
n,m=map(int,input().split())
arr = list(map(int,input().split()))
minValues(arr, n, m) 
