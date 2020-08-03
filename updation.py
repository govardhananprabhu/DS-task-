"""
Question
Mahesh is a product developer,he wants to update his product but there are lot of
works,so he split's the work and gave you an important work.The work is to update
the array elements,the elements are the key for updation.
note:
Given an array arr[] of n integers, construct a Update Array Upd[] (of same size)
such that Upd[i] is equal to the product of all the elements of arr[] except arr[i].

Input description
First line has size of array
Second line has array elements(integers)
Output description
print the updated array

Explanation
Input: arr[]  = {10, 3, 5, 6, 2}
Output: Upd[]  = {180, 600, 360, 300, 900}
3 * 5 * 6 * 2 product of other array 
elements except 10 is 180
10 * 5 * 6 * 2 product of other array 
elements except 3 is 600
10 * 3 * 6 * 2 product of other array 
elements except 5 is 360
10 * 3 * 5 * 2 product of other array 
elements except 6 is 300
10 * 3 * 6 * 5 product of other array 
elements except 2 is 900

Input
5
1 2 3 4 5
Output
120 60 40 30 24 

Input
6
1 0 3 5 4 2
Output
0 120 0 0 0 0

Input
2
1 2
Output
2 1

Input
1
1
Output
0

Input
4
55 4 3 99
Output
1188 16335 21780 660
Hint
To get the product excluding that index,multiply the prefix product up to index
i-1 with the suffix product up to index i+1.

Solution"""
def productArray(arr, n): 
	if(n == 1): 
		print(0) 
		return 
	left = [0]*n 
	right = [0]*n  
	prod = [0]*n  
	left[0] = 1
	right[n - 1] = 1
	for i in range(1, n): 
		left[i] = arr[i - 1] * left[i - 1] 
	for j in range(n-2, -1, -1): 
		right[j] = arr[j + 1] * right[j + 1]
	for i in range(n): 
		prod[i] = left[i] * right[i] 
	for i in range(n): 
		print(prod[i], end =' ') 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
productArray(arr, n) 
