"""
Given an integer N,print the Hosoya’s triangle with the range N.

H 7
T 2000
Tag accolite patterns mathematics

In des
First line contain integer N, denotes the range.

Ot des
Print the pattern till the range.

5
1 
1 1 
2 1 2 
3 2 2 3 
5 3 4 3 5

2
1 
1 1

3
1 
1 1 
2 1 2

4
1 
1 1 
2 1 2 
3 2 2 3

7
1 
1 1 
2 1 2 
3 2 2 3 
5 3 4 3 5 
8 5 6 6 5 8 
13 8 10 9 10 8 13 

Exp
From sample:
The two outermost diagonals are the Fibonacci numbers.All the other numbers in the triangle are the product of two distinct Fibonacci numbers greater than 1. The row sums are the first convolved Fibonnaci numbers.
Hint
The Fibonnaci triangle or Hosoya’s triangle is a triangular arrangement of numbers based on Fibonacci numbers. Each number is the sum of two numbers above in either the left diagonal or the right diagonal.

"""

def Hosoya( n , m ):  
	if ((n == 0 and m == 0) or
		(n == 1 and m == 0) or
		(n == 1 and m == 1) or
		(n == 2 and m == 1)): 
				return 1
	
	if n > m: 
		return Hosoya(n - 1, m) + Hosoya(n - 2, m) 

	elif m == n: 
		return Hosoya(n - 1, m - 1) + Hosoya(n - 2, m - 2) 

	else: 
		return 0
 
def printHosoya( n ): 
	for i in range(n): 
		for j in range(i + 1): 
			print(Hosoya(i, j) , end = " ") 
		print("\n", end = "") 

n = int(input())
printHosoya(n) 


