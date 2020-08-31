"""
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

In des
First line contain integer N,denotes dimension of matrix
Next N line contains N space separated zeroes.

Ot des
Print the N*N board with 1 denotes queen in matrix


4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

0 0 1 0 
1 0 0 0 
0 0 0 1 
0 1 0 0

Exp
From sample
The expected output is a binary matrix which has 1s for the blocks where queens are placed. Following is the output matrix for above 4 queen solution.

              { 0,  1,  0,  0}
              { 0,  0,  0,  1}
              { 1,  0,  0,  0}
              { 0,  0,  1,  0}

Hint
Generate all possible configurations of queens on board and print a configuration that satisfies the given constraints.

H 8
T 2000
"""
N = int(input())
ld = [0] * 30
rd = [0] * 30
cl = [0] * 30
def printSolution(board): 
	for i in range(N): 
		for j in range(N): 
			print(board[i][j], end = " ") 
		print() 
def solveNQUtil(board, col): 
	if (col >= N): 
		return True
	for i in range(N): 
		if ((ld[i - col + N - 1] != 1 and
			rd[i + col] != 1) and cl[i] != 1): 
			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
			if (solveNQUtil(board, col + 1)): 
				return True
			board[i][col] = 0 
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
	return False
def solveNQ(): 
	board = [[0, 0, 0, 0], 
			[0, 0, 0, 0], 
			[0, 0, 0, 0], 
			[0, 0, 0, 0]] 
	if (solveNQUtil(board, 0) == False): 
		printf("-1") 
		return False
	printSolution(board) 
	return True
solveNQ() 
