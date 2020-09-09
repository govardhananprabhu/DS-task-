"""
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.

H 6
T 2000
tag accolite array

In des
First line contains integer N,denotes size of array.
second line contains N space separated integers, denotes array elements.

Ot des
Print the rotations K

6
15 18 2 3 6 12

2

3
3 1 2

1

4
4 3 2 1

3

5
7 9 11 12 5

4

5
17 9 11 12 15

1
Exp
From sample:
Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Hint
we can notice that the number of rotations is equal to index of minimum element. A simple linear solution is to find minimum element and returns its index. Below is C++ implementation of the idea.
"""
def countRotations(arr, n): 
	min = arr[0] 
	for i in range(0, n): 
	
		if (min > arr[i]): 
		
			min = arr[i] 
			min_index = i 
		
	return min_index; 
N=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
print(countRotations(arr, n)) 


