"""
Given a binary array and an integer m, find the position of zeroes flipping which creates maximum number of consecutive 1’s in array

H 7
T 2300
Tag accolite array

In des
First line contains integer N,size of array.
Second line contains N space separated integers,denotes array elements.
Third line contains a single integer.

Ot des
Print the positions
12
1 0 0 1 1 0 1 0 1 1 1
2

5 7

11
1 0 0 1 1 0 1 0 1 1 1
1

7

4
0 0 0 1
4
0 1 2

4
1 0 1 1
3
1

2
0 0
2
0 1 

Exp
We are allowed to flip maximum 2 zeroes. If we flip
arr[5] and arr[7], we get 8 consecutive 1's which is
maximum possible under given constraint

Hint
A Simple Solution is to consider every subarray by running two loops. For every subarray, count number of zeroes in it. Return the maximum size subarray with m or less zeroes.

"""
def findZeroes(arr, n, m) : 
	wL = wR = 0
	bestL = bestWindow = 0
	zeroCount = 0

	while wR < n: 
		
		if zeroCount <= m : 
			if arr[wR] == 0 : 
				zeroCount += 1
			wR += 1
		if zeroCount > m : 
			if arr[wL] == 0 : 
				zeroCount -= 1
			wL += 1
		if (wR-wL > bestWindow) and (zeroCount<=m) : 
			bestWindow = wR - wL 
			bestL = wL 

	for i in range(0, bestWindow): 
		if arr[bestL + i] == 0: 
			print (bestL + i, end = " ") 
N=int(input())
arr = list(map(int,input().split()))
m = int(input())
n = len(arr)  
findZeroes(arr, n, m) 
