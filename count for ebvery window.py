"""
Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k.

H 6
T 2000
Tag accolite array

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers,denotes array elements.
Third line contains an integer K.

7
1 2 1 3 4 2 3
4

3 4 4 3

4
1 2 4 4
2
2 2 1

3
1 4 6
2
2 2

2
1 3
1
1 1

6
1 2 1 1 4 5
3
2 2 2 3 
Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

Hint
The naive solution is to traverse the given array considering every window in it and keeping a count on the distinct elements of the window.
"""
import math as mt 
def countWindowDistinct(win, k): 

	dist_count = 0
	for i in range(k):  
		j = 0
		while j < i: 
			if (win[i] == win[j]): 
				break
			else: 
				j += 1
		if (j == i): 
			dist_count += 1
	
	return dist_count 
def countDistinct(arr, n, k): 
	for i in range(n - k + 1): 
		print(countWindowDistinct(arr[i:k + i], k),end=" ") 
N=int(input())
arr = list(map(int,input().split())) 
k = int(input())
n = len(arr) 
countDistinct(arr, n, k) 

# This code is contributed by 
# Mohit kumar 29 
