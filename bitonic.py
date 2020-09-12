"""
Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first increasing, then decreasing. Write a function that takes an array as argument and returns the length of the longest bitonic subsequence.
A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.

H 6
T 2500
Tag cisco array

In des
First line contain integer N,size of array.
Second line contains N space integers,denotes array elements.

Ot des
Print the length of sequence


8
1 11 2 10 4 5 2 1

6

6
12 11 40 5 3 1

5

6
80 60 30 40 20 10

5

7
1 32 4 3 7 6 9

4

3
1 2 3

3


Exp
From sample:
A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1

Hint
Let the input array be arr[] of length n. We need to construct two arrays lis[] and lds[] using Dynamic Programming solution of LIS problem. lis[i] stores the length of the Longest Increasing subsequence ending with arr[i]. lds[i] stores the length of the longest Decreasing subsequence starting from arr[i]. Finally, we need to return the max value of lis[i] + lds[i] – 1 where i is from 0 to n-1.
"""
def lbs(arr): 
	n = len(arr) 
	lis = [1 for i in range(n+1)] 
	for i in range(1 , n): 
		for j in range(0 , i): 
			if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
				lis[i] = lis[j] + 1
	lds = [1 for i in range(n+1)]  
	for i in reversed(range(n-1)): 
		for j in reversed(range(i-1 ,n)):
			if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 
				lds[i] = lds[j] + 1
	maximum = lis[0] + lds[0] - 1
	for i in range(1 , n): 
		maximum = max((lis[i] + lds[i]-1), maximum) 
	
	return maximum
N =int(input())
arr = list(map(int,input().split()))
print(lbs(arr)) 
