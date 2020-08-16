"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

In des
First line contain integer N,denotes size of array
Second line contain N space separated integers,denotes prices in array elements.

Ot des
Print the maximum obtainable value.
8
1 5 8 9 10 17 17 20
22

8
3 5 8 9 10 17 17 20
24
EXP
For example, if length of the rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

H 5
T 2000


"""
import sys  
def max(a, b): 
	return a if (a > b) else b 
def cutRod(price, n): 
	if(n <= 0): 
		return 0
	max_val = -sys.maxsize-1
	for i in range(0, n): 
		max_val = max(max_val, price[i] +
					cutRod(price, n - i - 1)) 
	return max_val
N=int(input())
arr = list(map(int,input().split()))
size = len(arr) 
print(cutRod(arr, size)) 
