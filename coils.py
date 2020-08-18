"""
Given a positive integer n that represents dimensions of a 4n x 4n matrix with values from 1 to n filled from left to right and top to bottom. Form two coils from matrix and print the coils.

In des
First line contain integer N,denotes the dimensions.

Ot des
Print first coil in first line.
Print second coil in second line.

EXp
From sample
Matrix is 
1  2  3  4 
5  6  7  8 
9  10 11 12 
13 14 15 16

Hint
Total elements in matrix are 16n2. All elements are divided in two coils. Every coil has 8n2 elements. We make two arrays of this size. We first fill elements in coil1 by traversing in given order. Once we have filled elements in coil1, we can get elements of other coil2 using formula coil2[i] = 16*n*n + 1 -coil1[i].

H-7
T-3000

""" 
def printCoils(n): 
	m = 8*n*n 
	coil1 = [0]*m  
	coil1[0] = 8*n*n + 2*n 
	
	curr = coil1[0] 
	
	nflg = 1
	step = 2 
	index = 1
	while (index < m): 
		
		for i in range(step): 
			 
			curr = coil1[index] = (curr - 4*n*nflg) 
			index += 1
			if (index >= m): 
				break
		if (index >= m): 
			break
		for i in range(step): 
			
			curr = coil1[index] = curr + nflg 
			index += 1
			if (index >= m): 
				break
		nflg = nflg*(-1) 
		step += 2
	
	
	coil2 = [0]*m 
	i = 0
	while(i < 8*n*n): 
		coil2[i] = 16*n*n + 1 -coil1[i] 
		i += 1
	i = 0
	while(i < 8*n*n): 
		print(coil1[i], end = " ") 
		i += 1
	print("\n", end = " ") 
	i = 0
	while(i < 8*n*n): 
		print(coil2[i], end = " ") 
		i += 1


n = int(input())
printCoils(n) 
