"""
Given two unsorted arrays that represent two sets , find intersection of two arrays.

H 5 T 2000
Tag Accolite Array

In des
First line contains 2 integer N,M, denotes size of arrays.
Second line contains N space separated integers,denotes array elements.
Third line contains M space separated integers,denotes array elements.

Ot des
Print the intersection of 2 arrays.


8 3
1 2 3 3 4 5 5 6 
3 3 5
3 3 5

3 3
1 2 3
1 4 5
1 

5 6
1 4 3 2 5
1 4 6 8 9 1
1 4

4 2
1 3 6 8
2 8
8

2 1
1 3
1
1

Exp
From sample
1 is the intersection of given 2 array

Hint
Print the elements present in both the arrays.



""" 
def intersection(a, b, n, m): 

	i = 0
	j = 0
	
	while (i < n and j < m) : 
				
		if (a[i] > b[j]) : 
			j += 1
				
		else: 
			if (b[j] > a[i]) : 
				i += 1

			else: 
				print(a[i], end = " ") 
				i += 1
				j += 1
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
intersection(a, b, n, m) 

