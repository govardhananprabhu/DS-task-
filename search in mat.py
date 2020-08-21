"""
Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity.


In des
First line contain two space separated integers R,C, denotes dimensions of matrix.
Next R lines contain C space separated integers,denotes matrix elements.
Third line contain integer X,denotes element to be founded.

Ot des
Print the index i,j of founded element.if not print "Element not found".

4 4
10 20 30 40
15 25 35 45
27 29 37 48
32 33 39 50
29

2 1

Exp
From sample
Element found at (2,1)

Hint
The simple idea is to traverse the array and to search element one by one.

H 6
T 3000


""" 
def search(mat, n, x): 

	i = 0
	j = n - 1
	while ( i < n and j >= 0 ): 
	
		if (mat[i][j] == x ): 
	
			print(i, j) 
			return 1
	
		if (mat[i][j] > x ): 
			j -= 1
		else: 
			i += 1
	
	print("Element not found") 
	return 0  
R,C=map(int,input().split())
mat=[]
for i in range(R):
    l=list(map(int,input().split()))
    mat.append(l)
X=int(input())
search(mat, R, X) 
