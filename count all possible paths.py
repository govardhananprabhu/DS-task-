"""
The task is to count all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.

H 6
T 2500

Tag cisco,ola cabs,matrix

In des
First line consists of N and M, denoting the number of rows and number of column respectively.

Ot des
Single line output, count of all the possible paths from top left to bottom right of a mXn matrix.

2 2

2

2 3

3

3 3

6

4 3

10

1 1

1



From sample:
There are two paths
(0, 0) -> (0, 1) -> (1, 1),
(0, 0) -> (1, 0) -> (1, 1)
Hint
If either given row number is first or given column number is first return 1, use recursive function to recursively increase th path's count by reducing row size and column size recursively. 
""" 
def numberOfPaths(m, n):
	if(m == 1 or n == 1): 
		return 1

	return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 

m,n=map(int,input().split())
print(numberOfPaths(m, n)) 

