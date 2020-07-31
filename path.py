"""
Question
Given two sorted arrays, such that the arrays may have some common elements. Find the sum of the maximum sum path to reach from the beginning of any array to end of any of the two arrays. We can switch from one array to another array only at common elements.

Input description
First line has length of two arr
Second line has arr1
Third line has arr2
Output description
print the sum
Explanation
Input: ar1[] = {2, 3, 7, 10, 12}
       ar2[] = {1, 5, 7, 8}
Output: 35

Explanation: 35 is sum of 1 + 5 + 7 + 10 + 12.
We start from the first element of arr2 which is 1, then we
move to 5, then 7.  From 7, we switch to ar1 (as 7 is common)
and traverse 10 and 12.

Input
2 2
1 2 3
1 2 3
Output
6

Input
5 4
4 3 2 6 7
3 2 4 5
Output
27

Input
1 2
1
1 2
Output
3

Hint
This involves calculating the sum of elements between all common points of both arrays. Whenever there is a common point, compare the two sums and add the maximum of two to the result.
Solution:"""
def maxPathSum(ar1,ar2 , m , n):  
	i, j = 0, 0 
	result, sum1, sum2= 0, 0, 0 
	while (i < m and j < n): 
		if ar1[i] < ar2[j]: 
			sum1 += ar1[i] 
			i+=1 
		elif ar1[i] > ar2[j]: 
			sum2 += ar2[j] 
			j+=1
		
		else: 
			result+= max(sum1,sum2)
			sum1, sum2 = 0, 0
			while (i < m and j < n and ar1[i]==ar2[j]): 
				result += ar1[i] 
				i+=1
				j+=1
	while i < m: 
		sum1 += ar1[i] 
		i+=1
	while j < n: 
		sum2 += ar2[j] 
		j+=1
	result += max(sum1,sum2) 
	
	return result
N,M=map(int,input().split())
ar1 = list(map(int,input().split())) 
ar2 = list(map(int,input().split()))
m = len(ar1) 
n = len(ar2) 
print(maxPathSum(ar1, ar2, m, n))
