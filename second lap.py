"""
There are some Atheletes running in a ground,Given an array of integers which denotes atheletes, find the first athelete who started runing second lap in it.The lap count is equal to count of an element in array.If no one started print -1.

In des
First line contain N integer,denotes size of array.
Second line contain N space separated integers,denotes atheletes.

Ot des
Print the athelete who started second lap first.

7
10 5 3 4 3 5 6

5


9
6 10 5 4 9 120 4 6 10

6



Exp
From sample
5 is the first element that repeats.

Hint
Traverse the array, once we find an element that repeats first, print the element.

H 5
T 2000

"""
def printFirstRepeating(arr, n):  
	Min = -1 
	myset = dict() 
	for i in range(n - 1, -1, -1): 
		if arr[i] in myset.keys(): 
			Min = i 

		else:  
			myset[arr[i]] = 1
	if (Min != -1): 
		print(arr[Min]) 
	else: 
		print("-1") 

N=int(input())
arr = list(map(int,input().split()))

n = len(arr) 
printFirstRepeating(arr, n) 

# This code is contributed by Mohit kumar 29 
