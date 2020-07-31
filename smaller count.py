"""
Question
Write a function to count number of smaller elements on right of each element in an array. Given an unsorted array arr[] of distinct integers, construct another array countSmaller[] such that countSmaller[i] contains count of smaller elements on right side of each element arr[i] in array.

Input description
First line has integer N
Second line has list of integers 
Output description
Print countSmaller array

Explanation
Input:   arr[] =  {12, 1, 2, 3, 0, 11, 4}
Output:  countSmaller[]  =  {6, 1, 1, 1, 0, 1, 0}

Input
5
1 2 3 4 5
Output
0 0 0 0 0

Input
6
5 4 3 2 6 7
Output
3 2 1 0 0 0

Input
8
1 3 2 6 5 9 2 1
Output
0 3 1 3 2 2 1 0

Input
5
5 4 3 2 1
Output
4 3 2 1 0

Input
1
1
Output
0

Hint
Use two loops. The outer loop picks all elements from left to right. The inner loop iterates through all the elements on right side of the picked element and updates countSmaller[].

"""
def constructLowerArray (arr, countSmaller, n):  
	for i in range(n): 
		countSmaller[i] = 0; 

	for i in range(n): 
		for j in range(i + 1,n): 
			if (arr[j] < arr[i]): 
				countSmaller[i] += 1
def printArray(arr, size): 
	for i in range(size): 
		print(arr[i],end=" ") 
	print()
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
low = [0]*n 
constructLowerArray(arr, low, n) 
printArray(low, n) 
