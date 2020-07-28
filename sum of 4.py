"""
Question
Given an array of integers,Avengers wants to team up to defeat thanos but there
should be four members at a team,find all combination of four members in the array
whose powers sum is equal to a given power of thanos X.


Input description
First line has array of integers has powers
Second line has power of thanos in integer

Output description
print the possible four power line by line

Explanation
if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and X = 23, then your function
should print “3 5 7 8” (3 + 5 + 7 + 8 = 23).

Input
1 2 3 4 5 6
14
Output
1 2 5 6
1 3 4 6
2 3 4 5

Input
2 3 4 5 6 7
8
Output
-1

Input
1 1 1 1 1 1 1 1 1
5
Output
-1

Input
222 33 43 21 56 73 54
47
Output
-1

Input
100 200 300 400 500
1000
Output
100 200 300 400

Hint
A Naive Solution is to generate all possible quadruples and compare the sum of every quadruple with X.
"""
def find4Numbers(A, n, X): 
	A.sort() 
	for i in range(n - 3): 
		for j in range(i + 1, n - 2): 
			l = j + 1
			r = n - 1
	
			while (l < r): 
				if(A[i] + A[j] + A[l] + A[r] == X): 
					print(A[i], A[j], 
						A[l], A[r])
					res.append(A[i])
					l += 1
					r -= 1
				
				elif (A[i] + A[j] + A[l] + A[r] < X): 
					l += 1
				else:  
					r -= 1
 
if __name__ == "__main__": 
	
	A = list(map(int,input().split()))
	ans=[]
	res=[]
	X = int(input())
	n = len(A) 
	find4Numbers(A, n, X)
if(len(res)==0):
    print(-1)


    
