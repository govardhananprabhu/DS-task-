"""
Question
Assume you are playing game,you need to crack a puzzle by finding number.Given
two numbers N and A, find N-th root of A. In mathematics, Nth root of a number
A is a real number that gives A, when we raise it to integer power N.

Input description
First line has integer N
Second line has integer A

Output description
print the value A upto 2 decimal

Explanation
Input : A = 81
        N = 4
Output : 3 
3^4 = 81

Input
81
4
Output
3.0

Input
36
5
Output
2.05

Input
4
2
Output
2.0

Input
1
1
Output
1.0

Input
99
9
Output
1.67

Hint
Using above relation, we can solve the given problem. In below code we iterate over values of x, until difference between two consecutive values of x become lower than desired accuracy.
Solution:"""
import math 
import random 
def nthRoot(A,N):
	xPre = random.randint(1,101) % 10 
	eps = 0.001
	delX = 2147483647
	xK=0.0
	while (delX > eps): 

		xK = ((N - 1.0) * xPre +
			A/pow(xPre, N-1)) /N 
		delX = abs(xK - xPre) 
		xPre = xK; 
		
	return xK 

A = int(input()) 
N = int(input())

nthRootValue = nthRoot(A, N) 

print(round(nthRootValue,2)) 


