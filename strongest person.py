"""
You are given with array elements of size N,the elements denotes persons,your task is to find the stronger person,
strongest element is,when no element in the right end side of arr[i] is greater than arr[i].No need to consider the last person.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes persons in array.

Ot des
Print the strongest person

7
2 7 5 3 0 8 1
8

Exp
From sample
There is no stronger person in the right of 8.

Hint
Traverse the array and for each element check it is greater than all the next elements.

H 5
T 2500
"""
def findSurpasser(arr, n):
    for i in range(0, n-1):
        count = 0;
        for j in range (i + 1, n):
            if (arr[j] > arr[i]):
                count += 1
        if(count==0):
            print(arr[i])
	
N=int(input()) 
arr = list(map(int,input().split()))
n = len(arr) 
findSurpasser(arr , n) 
