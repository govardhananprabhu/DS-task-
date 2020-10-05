"""
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

In des
First line contains integer N, size of array.
second line contains N space separated integers,denotes array elements.
Third line contains an integer N,denotes sum.

Ot des
Print the count of sum

4
1 5 7 -1
6

2

5
1 5 7 -1 5
6

3

4
1 1 1 1
2

6

13
10 12 10 15 -1 7 6 5 4 2 1 1 1
11

9

6
1 32 5 5 6 90
122

1
Exp
From sample:
Pairs with sum 6 are (1, 5) and (7, -1)

Hint
A simple solution is be traverse each element and check if there’s another number in the array which can be added to it to give sum.


"""
def getPairsCount(arr, n, sum): 
	
	count = 0 
	for i in range(0, n): 
		for j in range(i + 1, n): 
			if arr[i] + arr[j] == sum: 
				count += 1
	
	return count 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
sum = int(input())
print(getPairsCount(arr, n, sum))
