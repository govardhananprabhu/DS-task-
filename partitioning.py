"""
Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVVal come next.
3) All elements greater than highVVal appear in the end.

Input description
First line has size of array N
Second line has l,h high and low integer value
Third line has array elements(Integers)
Output description
print updated array

Input
13
14 20
1 14 5 20 4 2 54 20 87 98 3 1 32
Output
1 5 4 2 1 3 14 20 20 98 87 32 54

Input
5
3 4
1 2 3 4 5
Output
1 2 3 4 5

Input
6
4 8
1 2 99 55 3 4
Output
1 2 3 4 55 99

Input
2
1 2
3 4
Output
4 3

Input
3
1 3
1 2 3
Output
1 2 3

Hint
We traverse given array elements from left. We keep track of two pointers, first (called start in below code) to
store next position of smaller element (smaller than range) from beginning; and
second (called end in below code) to store next position of greater element from end
Solution:"""
def threeWayPartition(arr, n, lowVal, highVal): 
	start = 0
	end = n - 1
	i = 0
	while i <= end: 
 
		if arr[i] < lowVal: 
			temp = arr[i] 
			arr[i] = arr[start] 
			arr[start] = temp 
			i += 1
			start += 1
		elif arr[i] > highVal: 
			temp = arr[i] 
			arr[i] = arr[end] 
			arr[end] = temp 
			end -= 1

		else: 
			i += 1

N=int(input())
l,h=map(int,input().split())
arr = list(map(int,input().split()))
n = len(arr) 

threeWayPartition(arr, n, l, h) 
print(*arr) 
