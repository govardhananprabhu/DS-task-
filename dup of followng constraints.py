"""
Given a sorted array having 10 elements which contains 6 different numbers in which only 1 number is repeated five times. Your task is to find the duplicate number using two comparisons only.

H 4
T 2000
Tag yahoo,array

In des
First line contains 10 space separated values of the array A[].

Ot des
Print the required duplicate element.

1 1 1 1 1 5 7 10 20 30

1

1 2 3 3 3 3 3 5 9 10

3

1 2 2 2 2 2 3 5 9 10

2

0 0 0 0 3 6 8 9 11 0
0

12 34 55 34 34 34 67 72 88 34

34S
Exp
From sample element 1 repeated 5 times in array.

Hint
An important observation is, arr[4] or arr[5] is an occurrence of repeated element for sure.

""" 
def findDuplicate(a): 

	if (a[3] == a[4]): 
		return a[3] 
	elif (a[4] == a[5]): 
		return a[4] 
	else: 
		return a[5] 
a = list(map(int,input().split()))
print(findDuplicate(a)) 
