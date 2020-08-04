"""
Given a sorted array containing only numbers 0 and 1, the task is to find the epic
point efficiently. The epic point is a point where “0” ends and “1” begins.

Input description
First line has N size of array
Second line has array elements

Output description
Print the epic point else "no epic point"

Explanation
Input: 0 0 0 1 1
Output: 3

Explantion: Index of first 1 is 3

Input
3
1 1 1
Output
1

Input
2
0 1
Output
1

Input
9
0 0 0 0 0 0 0 0 1
Output
8

Input
1
0
Output
no epic point

Input
5
0 0 0 0 0
Output
no epic point

Hint
Traverse the array and print the index of the first 1
"""
def findTransitionPoint(arr, n): 

	for i in range(n): 
		if(arr[i] == 1): 
			return i 
	return -1
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 

point = findTransitionPoint(arr, n) 

if point >= 0: 
	print(point) 
else: 
	print("no epic point") 
