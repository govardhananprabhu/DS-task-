"""
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.

In des
First line contain integer N,size of element.
Second line contain N space separated integers, denotes array elements.

Ot des
Print the max diff
7
2 3 10 6 4 8 1
8

6
7 9 5 6 3 2
2


Exp
From sample
The maximum difference is between 10 and 2.


Hint
Use two loops. In the outer loop, pick elements one by one and in the inner loop calculate the difference of the picked element with every other element in the array and compare the difference with the maximum difference calculated so far.

H 5
T 2000
""" 
def maxDiff(arr, arr_size): 
	max_diff = arr[1] - arr[0] 
	
	for i in range( 0, arr_size ): 
		for j in range( i+1, arr_size ): 
			if(arr[j] - arr[i] > max_diff): 
				max_diff = arr[j] - arr[i] 
	
	return max_diff 
N=int(input())
arr = list(map(int,input().split())) 
size = len(arr) 
print (maxDiff(arr, size)) 
