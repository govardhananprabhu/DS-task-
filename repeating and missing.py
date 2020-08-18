"""
Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes the array elements.

Ot des
Print two space separated integers,which are missing and duplicate elements.
3
3 1 3
2 3

6
4 3 6 2 1 1
5 1

Exp
In the array, 
2 is missing and 3 occurs twice 

Hint
Sort the input array.
Traverse the array and check for missing and repeating.

H 5
T 2000



"""

def printTwoElements( arr, size): 
	for i in range(size): 
		if arr[abs(arr[i])-1] > 0: 
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1] 
		else: 
			print(abs(arr[i])) 
			
	for i in range(size): 
		if arr[i]>0: 
			print(i + 1)
N=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
printTwoElements(arr, n) 

# This code is contributed by "Abhishek Sharma 44" 
