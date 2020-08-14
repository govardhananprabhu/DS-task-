"""
Given two binary arrays arr1[] and arr2[] of same size n. Find length of the smallest common span (i, j) where j >= i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].

In des
First line contain integers N,size of two arr.
Second line contain N space separated integrs,denotes arr1 elements.
Second line contain N space separated integrs,denotes arr2 elements.

Ot des
Print the length of span

H-5
T-1000

sample
5
1 3 2 4 5
3 2 3 5 4

2

exp
From sample
The smallest span with same sum is from index 1 to 2.

Hint
One by one by consider same subarrays of both arrays. For all subarrays, compute sums and if sums are same and current length is less than min length, then update min length.
3
1 2 3
1 3 2
1

5
1 3 2 4 5
3 2 3 4 5
1

4
1 3 2 6 9
3 1 6 9 2
2


1
1
1
1

Array

"""

def smallestCommonSum(arr1, arr2, n): 
 
	minLen = n 

	for i in range(0,n): 
		sum1 = 0
		sum2 = 0

		for j in range(i,n): 
			sum1 += arr1[j] 
			sum2 += arr2[j] 
			if (sum1 == sum2): 
				len = j-i+1
				if (len < minLen): 
					minLen = len
	
	return minLen 
N=int(input()) 
arr1 = list(map(int,input().split())) 
arr2 = list(map(int,input().split())) 
n = len(arr1) 
print(smallestCommonSum(arr1, arr2, n)) 


