"""
Given a sorted array and a value x,you need to find hidden number,the hidden
num of x is the largest element in array smaller than or equal to x. Write
efficient functions to find hidden number of x.



Input description
First line has size of array
Second line has array elements
Third line has x element

Output description
Print the num or 'no'

Explanation
Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2
2 is the largest element in 
arr[] smaller than 5.


Input
5
1 2 3 4 5
5
Output
5


Input
7
3 2 4 5 9 66 44
55
Output
44

Input
1
1
1
Output
1

Input
4
1 3 2 4
5
Output
4

Input
6
3 5 4 2 6 7
1
Output
no


Hint
The idea is simple, traverse through the array and find the first element greater than x. The element just before the found element is the floor of x.
"""
def floorSearch(arr, low, high, x): 
	if (low > high): 
		return -1 
	if (x >= arr[high]): 
		return high 
	mid = int((low + high) / 2) 
	if (arr[mid] == x): 
		return mid 
	if (mid > 0 and arr[mid-1] <= x 
				and x < arr[mid]): 
		return mid - 1 
	if (x < arr[mid]): 
		return floorSearch(arr, low, mid-1, x) 
	return floorSearch(arr, mid + 1, high, x) 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
x = int(input())
arr.sort()
index = floorSearch(arr, 0, n-1, x) 

if (index == -1): 
	print("no") 
else: 
	print(arr[index]) 

 
