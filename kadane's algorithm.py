"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

In des
The first line contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Ot des
Print the maximum sum of the contiguous sub-array.

5
1 2 3 -2 5

9

4
-1 -2 -3 -4

0

13
-13 -3 -25 -20 -3 -16 -23 -12 -5 -22 -15 -4 -7

0

8
-2 -3 4 -1 -2 1 5 -3

7

5
1 -1 3 4 -3

7

From sample
Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.


Hint
Simple idea of the Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far

1000
7

"""
def maxSubArraySum(a,size): 
	
	max_so_far = 0
	max_ending_here = 0
	
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if max_ending_here < 0: 
			max_ending_here = 0
		elif (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
			
	print(max_so_far) 
N=int(input())
L=list(map(int,input().split()))
maxSubArraySum(L,N)
