"""
Given an array of integers. Find the first Don element in it. An array element is a Don if it is NOT smaller than its neighbours.

Input description
First line has size of array
Second line has array of integers
Output description
print the don

Explanation
Input: array[]= {5, 10, 20, 15}
Output: 20
The element 20 has neighbours 10 and 15,
both of them are less than 20.

Input
4
33 34 44 11
Output
44
Input
8
1 2 3 4 5 6 8 7
Output
8
Input
1
1
Output
1
Input
3
1 4 3
Output
4
Input
5
1 3 2 5 4
Output
3
Hint
The array can be traversed and the element whose neighbours are less than that element can be returned.

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

