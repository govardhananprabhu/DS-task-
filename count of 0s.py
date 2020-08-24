"""
Suppose we have an array.The content of the array is such that the first of the entries are 1s and the rest are all 0s. Write a function which will take this array as a parameter and return the number of 0s.

In des
The first line contains an integer N, where N is the size of the array A[ ].
The second line contains N space separated integers of all 1's follwed by all the 0's, denoting elements of the array A[ ].
ot des
Print out the number of 0's in the array.

6
1 1 1 1 0 0

2

5
1 0 0 0 0

4

3
0 0 0
3

4
1 1 1 1

0

1
1
0

Exp
From sample
there are 2 0s in given array

Hint
A simple solution is to traverse the input array. As soon as we find a 0, we return n – index of first 0. Here n is number of elements in input array. 


H 5
T 1000
"""
def firstZero(arr, low, high): 

	if (high >= low): 
		mid = low + int((high - low) / 2) 
		if (( mid == 0 or arr[mid-1] == 1) 
					and arr[mid] == 0): 
			return mid 
		if (arr[mid] == 1): 
			return firstZero(arr, (mid + 1), high) 
		else: 
			return firstZero(arr, low, (mid - 1)) 
	
	return -1
def countZeroes(arr, n): 
	first = firstZero(arr, 0, n - 1) 
	if (first == -1): 
		return 0

	return (n - first) 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
print(countZeroes(arr, n)) 

