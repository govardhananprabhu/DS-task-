"""
You are given with array elements of size N,the elements denotes persons,your task is to find the weakest person,
weakest element is,which person has the most greater persons on the right side of him.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes persons in array.

Ot des
Print the weakest person

7
2 7 5 3 0 8 1
2

7
5 7 5 3 0 8 1
5
Exp
From sample
Person 2 has 4 person greater than him. 

Hint
Traverse the array and for each element check it has most greater persons on right side of it.

H 5
T 2500
"""
def findSurpasser(arr, n):
    max=0
    ans=0
    for i in range(0, n-1):
        count = 0;
        for j in range (i + 1, n):
            if (arr[j] > arr[i]):
                count += 1
        if(count>max):
            max=count
            ans=arr[i]
    print(ans)
	
N=int(input()) 
arr = list(map(int,input().split()))
n = len(arr) 
findSurpasser(arr , n) 
