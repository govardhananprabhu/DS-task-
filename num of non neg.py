"""
Given a number n (number of variables) and val (sum of the variables), find out how many such nonnegative integral solutions are possible.

H 5 T 2500

Tag math

In des
First line contains 2 space separated integers n, v, denotes number and sum of variables.

Ot des
print possibility copunt

5 1
5

5 4
70

3 5
21

1 1
1

5 7
330
Exp
x1 + x2 + x3 + x4 + x5 = 1
Number of possible solution are : 
(0 0 0 0 1), (0 0 0 1 0), (0 0 1 0 0),
(0 1 0 0 0), (1 0 0 0 0)
Total number of possible solutions are 5

Hint
Count the solutions recursively with the given data.
"""
def countSolutions(n, val): 
	total = 0
	if n == 1 and val >=0: 
		return 1 
	for i in range(val+1): 
		total += countSolutions(n-1, val-i) 
	return total 
 
n, val = map(int,input().split())
print(countSolutions(n, val)) 
