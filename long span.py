"""
Given two binary arrays arr1[] and arr2[] of same size n,which has 1s denotes black rocks and 0s denotes white rocks. Find length of the longest common span (i, j) where j >= i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j],find the length of equal counts of black and white rocks in both arrays.

In des
First line contain integers N,size of two arr.
Second line contain N space separated integrs,denotes arr1 elements.
Second line contain N space separated integrs,denotes arr2 elements.

Ot des
Print the length of span

H-5
T-1000

sample
6 6
0 1 0 0 0 0
1 0 1 0 0 1

4

exp
From sample
The longest span with same sum is from index 1 to 4.

Hint
One by one by consider same subarrays of both arrays. For all subarrays, compute sums and if sums are same and current length is more than max length, then update max length.

4
0 0 1 0
1 1 1 1
1

3
0 0 0
1 1 1
0

7
0 1 0 1 1 1 1
1 1 1 1 1 0 1
6

1
1
1
1

Array

"""

def longestCommonSum(arr1, arr2, n): 
 
	maxLen = 0

	for i in range(0,n): 
		sum1 = 0
		sum2 = 0

		for j in range(i,n): 
			sum1 += arr1[j] 
			sum2 += arr2[j] 
			if (sum1 == sum2): 
				len = j-i+1
				if (len > maxLen): 
					maxLen = len
	
	return maxLen 
N=int(input()) 
arr1 = list(map(int,input().split())) 
arr2 = list(map(int,input().split())) 
n = len(arr1) 
print(longestCommonSum(arr1, arr2, n)) 


