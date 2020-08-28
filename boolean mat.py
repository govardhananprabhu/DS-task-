"""
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of ith row and jth column as 1.

In des
The first line is r and c, r is the number of rows and c is the number of columns.
The next r lines contains c space separated integers,denotes array elements.

Ot des
Print the modified matrix

2 2
1 0
0 0

1 1
1 0

2 3
0 0 0
0 0 1

0 0 1
1 1 1

3 4
1 0 0 1
0 0 1 0
0 0 0 0

1 1 1 1
1 1 1 1
1 0 1 1

1 1
0 0

0 

1 1
1 0

1
1 
From sample:
 Since only first element of matrix has 1 (at index 1,1) as value, so first row and first column are modified to 1.

Hint
1) Create two temporary arrays row[M] and col[N]. Initialize all values of row[] and col[] as 0.
2) Traverse the input matrix mat[M][N]. If you see an entry mat[i][j] as true, then mark row[i] and col[j] as true.
3) Traverse the input matrix mat[M][N] again. For each entry mat[i][j], check the values of row[i] and col[j]. If any of the two values (row[i] or col[j]) is true, then mark mat[i][j] as true.

H 7
T 3000

"""

R,C=map(int,input().split())


def modifyMatrix(mat): 
	row = [0] * R 
	col = [0] * C 
	for i in range(0, R): 
		row[i] = 0 
	for i in range(0, C) : 
		col[i] = 0
	for i in range(0, R) : 
		
		for j in range(0, C) : 
			if (mat[i][j] == 1) : 
				row[i] = 1
				col[j] = 1
	for i in range(0, R) : 
		
		for j in range(0, C): 
			if ( row[i] == 1 or col[j] == 1 ) : 
				mat[i][j] = 1
def printMatrix(mat) : 
	for i in range(0, R): 
		
		for j in range(0, C) : 
			print(mat[i][j], end = " ") 
		print()  
mat=[]
for i in range(R):
    l=list(map(int,input().split()))
    mat.append(l)
modifyMatrix(mat) 
printMatrix(mat)
