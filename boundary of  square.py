"""Question
You are given with square matrix,the task is to print the boundary of the
square matrix

Input description
First line has R,C contains number of rows and columns,then R lines with C size.

Output description
print the boundary values in single line

Test cases

Input
3 3
1 2 3
1 2 3
1 2 3

Output
1 2 3 3 3 2 1 1 

Input
5 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

Output
1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 

Input
1 1
1
Output
1

Input
2 2
1 2
3 4

Output
1 2 4 3 

Input
4 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

Output
1 2 3 4 4 4 4 3 2 1 1 1 

Hints
Print first row first then print last column without first value,the print last
row without the last value,finally first column without first and last value.
Solution"""
def printdata(arr, i, j, m, n): 
	if (i >= m or j >= n): 
		return
	for p in range(i, n): 
		print(arr[i][p], end = " ") 
	for p in range(i + 1, m): 
		print(arr[p][n - 1], end = " ")  
	if ((m - 1) != i): 
		for p in range(n - 2, j - 1, -1): 
			print(arr[m - 1][p], end = " ")
	if ((n - 1) != j): 
		for p in range(m - 2, i, -1): 
			print(arr[p][j], end = " ") 
			


R,C =map(int,input().split())
arr=[]
for i in range(R):
    l=list(map(int,input().split()))
    arr.append(l)

		
printdata(arr, 0, 0, R, C) 

