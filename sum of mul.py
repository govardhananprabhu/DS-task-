"""
Given three integer A, B and N. The task is to find the sum of all the elements below N which are multiples of either A or B.

cisco mathematics
5
1000

in des
First line contains contains 3 integers.

Ot des
Print the sum

10 3 5

23

50 8 15

258

12 2 3
42

6 3 5
8

17 4 9
49


Exp
3, 5, 6 and 9 are the only numbers below 10 which are multiples of either 3 or 5

Hint
Find the values which are multiples of given integers by traversing and print the sum of multiples.


""" 
def findSum(n, a, b): 
	sum = 0
	for i in range(0, n, 1): 
		if (i % a == 0 or i % b == 0): 
			sum += i 

	return sum
n,a,b=map(int,input().split())
print(findSum(n, a, b))
