"""
Given two arrays which are duplicates of each other except one element, that is one element from one of the array is missing, we need to find that missing element.If the input is not sufficient print Invalid Input

H 6
T 2500
Tag accolite array

In des
First line contains 2 space separated 2 A,B integers, denotes size of two arrays.
Second line contains A space separated integers,denotes array elements.
Third line contains B space separated integers,denotes array elements.

Ot des
Print the missing element.

3 3
1 2 3
4 5 7

Invalid Input

5 3
1 3 4 5 6
1 5 6
Invalid Input

5 4
1 3 4 5 7
1 3 5 7
4

3 2
1 2 3
1 3
2

Exp
5 4
1 4 5 7 9
4 5 7 9

1

1 is missing from second array.

Hint
One simple solution is to iterate over arrays and check element by element and flag the missing element when an unmatch is found, but this solution requires linear time over size of array.
"""
def findMissingUtil(arr1, arr2, N): 
	if N == 1: 
		return arr1[0];  
	if arr1[0] != arr2[0]: 
		return arr1[0] 
	lo = 0
	hi = N - 1
	while (lo < hi): 
	
		mid = (lo + hi) // 2
		if arr1[mid] == arr2[mid]: 
			lo = mid 
		else: 
			hi = mid 
		if lo == hi - 1: 
			break
	return arr1[hi] 
 
def findMissing(arr1, arr2, M, N): 

	if N == M-1: 
		print(findMissingUtil(arr1, arr2, M)) 
	elif M == N-1: 
		print(findMissingUtil(arr2, arr1, N)) 
	else: 
		print("Invalid Input") 
a,b=map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
M = len(arr1) 
N = len(arr2) 
findMissing(arr1, arr2, M, N) 
