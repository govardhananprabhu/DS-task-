"""
Given an array of integers of size n. Assume ‘0’ as invalid number and all other as valid number. Convert the array in such a way that if next number is a valid number and same as current number, double its value and replace the next number with 0. After the modification, rearrange the array such that all 0’s are shifted to the end.

H 5 T 1500
Tag array

In des
First line contains integer N, denotes size of array.
Second line contains N space separated integers, denotes array elements.

Ot des
Print the altered array

6
2 2 0 4 0 8
4 4 8 0 0 0

10
0 2 2 2 0 6 6 0 0 8
4 2 12 8 0 0 0 0 0 0

4
1 2 3 4
1 2 3 4

6
1 3 4 4 0 8
1 3 8 8 0 0

3
2 2 2
4 2 0
Exp
Alter the array when the next value is same double it from sample the array is
4 4 8 0 0 0

Hint
First modify the array as mentioned, i.e., if next valid number is same as current number, double its value and replace the next number with 0.

""" 
def pushZerosToEnd(arr, n):  
	count = 0
	for i in range(0, n): 
		if arr[i] != 0: 
			arr[count] = arr[i] 
			count+=1
	while (count < n): 
		arr[count] = 0
		count+=1
def modifyAndRearrangeArr(ar, n):  
	if n == 1: 
		return
	for i in range(0, n - 1):  
		if (arr[i] != 0) and (arr[i] == arr[i + 1]):  
			arr[i] = 2 * arr[i]  
			arr[i + 1] = 0
			i+=1
	pushZerosToEnd(arr, n) 
def printArray(arr, n): 

	for i in range(0, n): 
		print(arr[i],end=" ")  
N=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
modifyAndRearrangeArr(arr, n) 
printArray(arr, n)
