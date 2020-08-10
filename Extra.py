"""
H-5
Given two sorted arrays. There is only 1 difference between the arrays. The first array has one element extra added in between. Find the index of the extra element.

Explanation: The first array has an extra element 9.
The extra element is present at index 4.

In des
First line contain two space integers N,M,size of arrays.
Second line contain N space separated integers,denotes the arr1 elements.
Second line contain M space separated integers,denotes the arr2 elements.
Ot des
print the extra element's index.

Hin
The basic method is to iterate through the whole second array and check element by element if they are different. As the array is sorted, checking the adjacent position of two arrays should be similar until and unless the missing element is found.
T-1500

1 1
3 5 7 9 11 13
3 5 7 11 13
3

7 6
2 4 6 8 9 10 12
2 4 6 8 10 12
4

4 2
1 3 6 8
1 3 4
2

1 1
1
2
0

3 2
1 2 3
1 3
1

"""
def findExtra(arr1, arr2, n) : 
	for i in range(0, n) : 
		if (arr1[i] != arr2[i]) : 
			return i 

	return n 


N,M=map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
n = len(arr2)  
print(findExtra(arr1, arr2, n)) 
