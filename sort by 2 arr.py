"""
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among the elements will be same as those are in A2. For the elements not present in A2, append them at last in sorted order.

H 6 T 2500
Tag array

In des
First line contains 2 space separated integers n,m, denotes arr1 and arr2 size.
Second line contains n space separated integers, denotes arr1 elements.
Third line contains m space separated integers, denotes arr2 elements.

Ot des
Print the sorted array

11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3

5 2
1 3 2 6 8
3 8
3 8 1 2 6

3 2
1 3 5
1 9
1 3 5

4 4
1 3 5 7
2 4 6 5
5 1 3 7

8 2
1 3 4 2 5 6 4 3
1 3
1 3 3 2 4 4 5 6

Exp
the sorted order of arr1 is arr1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}

HINT
The element 1st present in arr2 should come first in arr1 and so on for all the elements and the remaining elements should be arranged in ascending order at the last. 

"""
"""A Python 3 program to sort an array 
according to the order defined by 
another array"""

"""A Binary Search based function to find 
index of FIRST occurrence of x in arr[].
If x is not present, then it returns -1
"""

def first(arr, low, high, x, n) :
	if (high >= low) :
		mid = low + (high - low) // 2; 
		if ((mid == 0 or x > arr[mid-1]) and arr[mid] == x) :
			return mid
		if (x > arr[mid]) :
			return first(arr, (mid + 1), high, x, n)
		return first(arr, low, (mid -1), x, n)
		
	return -1

def sortAccording(A1, A2, m, n) :
	temp = [0] * m
	visited = [0] * m
	
	for i in range(0, m) :
		temp[i] = A1[i]
		visited[i] = 0
	temp.sort()
	ind = 0
	for i in range(0, n) :
		f = first(temp, 0, m-1, A2[i], m)

		if (f == -1) :
			continue
		j = f
		while (j<m and temp[j]== A2[i]) :
			A1[ind] = temp[j];
			ind = ind + 1
			visited[j] = 1
			j = j + 1
	
	for i in range(0, m) :
		if (visited[i] == 0) :
			A1[ind] = temp[i]
			ind = ind + 1
def printArray(arr, n) :
	for i in range(0, n) :
		print(arr[i], end = " ")
	print("")
m,n=map(int,input().split())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
sortAccording(A1, A2, m, n)
printArray(A1, m)
