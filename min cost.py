"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

In des
First line contain two space integers R,C,denotes the matrix dimensions
Next R lines contain C space separated integers,denotes matrix elements.
Third line contain two space separated integers a,b,denotes the element which's path to be found.

Ot des
Print the cost

Exp
The path is (0, 0) –> (0, 1) –> (1, 2) –> (2, 2). The cost of the path is 8 (1 + 2 + 2 + 3).

T 3000
H 6

3 3
1 2 3
4 8 2
1 5 3
2 2

8

H
The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.

"""
R,C=map(int,input().split())
import sys  
def minCost(cost, m, n): 
	if (n < 0 or m < 0): 
		return sys.maxsize 
	elif (m == 0 and n == 0): 
		return cost[m][n] 
	else: 
		return cost[m][n] + min( minCost(cost, m-1, n-1), 
								minCost(cost, m-1, n), 
								minCost(cost, m, n-1) ) 


def min(x, y, z): 
	if (x < y): 
		return x if (x < z) else z 
	else: 
		return y if (y < z) else z 



cost=[]
for i in range(R):
    l=list(map(int,input().split()))
    cost.append(l)
a,b=map(int,input().split())
print(minCost(cost, a, b)) 

