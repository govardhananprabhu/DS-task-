"""
A surpasser of an element of an array is a greater element to its right, therefore x[j] is a surpasser of x[i] if i < j and x[i] < x[j]. The surpasser count of an element is the number of surpassers. Given an array of distinct integers, for each element of the array find its surpasser count i.e. count the number of elements to the right that are greater than that element.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes array elements.

Ot des
Print the surpasser array

7
2 7 5 3 0 8 1
4 1 1 1 2 0 0

Exp
From sample
2 has 4 elements greater than it on the right end side,similarly for
7 has 1,5 has 1,3 has 1,0 has 2,8 has 0 and final element always has 0.

Hint
Traverse the array and for each element find the count of elements on the right end side which is greater than current.

H 5
T 2500
"""
def findSurpasser(arr, n): 

	for i in range(0, n):  
		count = 0; 

		for j in range (i + 1, n): 
			if (arr[j] > arr[i]): 
				count += 1

		print(count, end = " ") 
	
N=int(input()) 
arr = list(map(int,input().split()))
n = len(arr) 
findSurpasser(arr , n) 
