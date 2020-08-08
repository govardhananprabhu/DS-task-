"""
Given a boolean 2D array,every 1 denotes chocolates and 0 denotes biscuits
where each row is sorted. Find the row with the maximum number of chocolates.

In des
First line contains two space separated integers M,N,which denotes the dimensions of matrix.
Next for each M lines contains N space separated integers,denotes the values.


Ot des
print the row index


Exp
From sample
third row has 4 1s which is maximum

Hin
A simple method is to do a row wise traversal of the matrix, count the number of 1s in each row and compare the count with max.
Finally, return the index of row with maximum 1s.



IN
4 4
0 1 1 1
0 0 1 1
1 1 1 1  
0 0 0 0

Ot
2

In
3 2
0 1
1 1
0 0
ot
1


In
1 1
1
ot
0

In
2 2
1 1
0 0
ot
0


In
2 3
0 0 1
0 1 1
ot
1

T
1600
"""

def first( arr, low, high): 
	if high >= low: 

		mid = low + (high - low)//2

		if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1: 
			return mid 

		elif arr[mid] == 0: 
			return first(arr, (mid + 1), high) 

		else: 
			return first(arr, low, (mid - 1)) 
	return -1
 
def rowWithMax1s( mat): 
	

	R = len(mat) 
	C = len(mat[0]) 
	max_row_index = 0
	max = -1

	for i in range(0, R): 
		index = first (mat[i], 0, C - 1) 
		if index != -1 and C - index > max: 
			max = C - index 
			max_row_index = i 

	return max_row_index 

M,N=map(int,input().split())
mat=[]
for i in range(M):
    l=list(map(int,input().split()))
    mat.append(l)
print (rowWithMax1s(mat)) 

