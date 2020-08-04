"""
Given an array of integers. Find the first king element in it. An array element is a king
if it is NOT smaller than its neighbours. For corner elements, we need to consider only one
neighbour.


Input description
First line has size of array
Second line has array elements

Output description
print the first king

Explanation
Input: array[] = {10, 20, 15, 2, 23, 90, 67}
Output: 20 
The element 20 has neighbours 10 and 15, 
both of them are less than 20, similarly 90 has neighbous 23 and 67,
but 20 occured first.

Input
3
1 2 3
Output
3

Input
5
1 2 3 4 0
Output
4

Input
7
0 1 2 3 8 11 5
Output
11

Input
1
1
Output
1

Input
7
10 20 15 2 23 90 67
Output
20
Hint
The array can be traversed and the element whose neighbours are
less than that element can be returned

"""
def findPeakUtil(arr, low, high, n): 
	mid = low + (high - low)/2
	mid = int(mid)  
	if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
		(mid == n - 1 or arr[mid + 1] <= arr[mid])): 
		return mid 

	elif (mid > 0 and arr[mid - 1] > arr[mid]): 
		return findPeakUtil(arr, low, (mid - 1), n) 

	else: 
		return findPeakUtil(arr, (mid + 1), high, n)  
def findPeak(arr, n): 

	return findPeakUtil(arr, 0, n - 1, n) 


N=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
print(arr[findPeak(arr, n)]) 
	
