"""
Given an array of N numbers where values of the array represent memory sizes. The memory that is required by the system can only be represented in powers of 2. The task is to return the size of the memory required by the system.

H 4 T 1000
Tag array mathematics bit

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers, denotes array elements.

Ot des
Print the size of memory needed.

4
2 1 4 5
16

4
1 2 3 2
8

7
1 3 22 12 34 53 1233
2048

2
1 33
64

1
8
8

Exp
The sum of memory required is 12, 
hence the nearest power of 2 is 16.

Hint
The problem is a combination of summation of array elements and smallest power of 2 greater than or equal to N. Find the sum of array elements and then find the smallest power of 2 greater than or equal to N.
"""
def nextPowerOf2(n):  
	p = 1
	if (n and not(n & (n - 1))): 
		return n 
	while (p < n): 
		p <<= 1
	return p 
def memoryUsed(arr, n): 
	sum = 0

	for i in range(n): 
		sum += arr[i] 

	nearest = nextPowerOf2(sum) 

	return nearest 
n=int(input())
arr = list(map(int,input().split()))
print(memoryUsed(arr, n)) 

