"""
Given a sorted array A, size N, of integers; every element appears twice except for one. Find that element that appears once in array.

In des
The first line contains the size of the array, and the second line has the elements of the array.

Ot des
print the number that appears only once in the array.


11
1 1 2 2 3 3 4 50 50 65 65

4

11
1 1 3 3 4 5 5 7 7 8 8

4

11
1 1 3 3 4 4 5 5 7 7 8

8

1
1

1

2
1 1

-1

From sample:
4 is present once in array.

Hint
A Simple Solution is to traverse the array from left to right. Since the array is sorted, we can easily figure out the required element.

H 5
T 2000

"""

def search(arr, low, high):  
	if low > high: 
		return None

	if low == high: 
		return arr[low] 

	mid = int(low + (high - low)/2)
	if mid%2 == 0: 

		if arr[mid] == arr[mid+1]: 
			return search(arr, mid+2, high) 
		else: 
			return search(arr, low, mid) 

	else: 
	
		if arr[mid] == arr[mid-1]: 
			return search(arr, mid+1, high) 
		else: 
			return search(arr, low, mid-1) 

N=int(input())
arr = list(map(int,input().split())) 

result = search(arr, 0, N-1) 

if result is not None: 
	print(result) 
else: 
	print(-1)
