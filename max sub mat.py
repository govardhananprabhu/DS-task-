"""
Given a 2D array, find the maximum sum subarray in it.

In des
First line contain two space separated integers R,C,denotes dimensions of matrix.
Next R lines contain C space separated integers,denotes matrix elements. 
Ot des
Print the max sum of sub matrix


4 5
1 2 -1 -4 -20
-8 -3 4 2 1
3 8 10 1 3
-4 -1 1 7 -6

29

Exp
From sample
the max sub matrix sum is from (1,1) to (3,3).

Hint
This solution requires 6 nested loops –
4 for start and end coordinate of the 2 axis.
and 2 for the summation of the sub-matrix.


H 8
T 4500


""" 
def kadane(arr, start, finish, n): 
	Sum = 0
	maxSum = -999999999999
	i = None
	finish[0] = -1
	local_start = 0
	
	for i in range(n): 
		Sum += arr[i] 
		if Sum < 0: 
			Sum = 0
			local_start = i + 1
		elif Sum > maxSum: 
			maxSum = Sum
			start[0] = local_start 
			finish[0] = i  
	if finish[0] != -1: 
		return maxSum
	maxSum = arr[0] 
	start[0] = finish[0] = 0 
	for i in range(1, n): 
		if arr[i] > maxSum: 
			maxSum = arr[i] 
			start[0] = finish[0] = i 
	return maxSum 
def findMaxSum(M): 
	global ROW, COL 
	maxSum, finalLeft = -999999999999, None
	finalRight, finalTop, finalBottom = None, None, None
	left, right, i = None, None, None
	
	temp = [None] * ROW 
	Sum = 0
	start = [0] 
	finish = [0] 
	for left in range(COL): 
		temp = [0] * ROW 
		for right in range(left, COL): 
			for i in range(ROW): 
				temp[i] += M[i][right] 
			Sum = kadane(temp, start, finish, ROW) 
			if Sum > maxSum: 
				maxSum = Sum
				finalLeft = left 
				finalRight = right 
				finalTop = start[0] 
				finalBottom = finish[0] 
 
	print(maxSum) 


ROW,COL=map(int,input().split())
M = []
for i in range(ROW):
    l=list(map(int,input().split()))
    M.append(l)

findMaxSum(M) 

