"""
H=6
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

Exp
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Hin
Use two loops. Outer loop iterates through all the element and inner loop finds out whether the current index picked by the outer loop is equilibrium index or not.

I des
First line contain integer N,size of array.
Second line contain N space separated integers,denotes array elements.

O des
Print the equlibrium index else -1

T=2000

7
-7 1 5 2 -4 3 0
3

5
1 4 3 -1 -2
-1

5
3 2 4 1 5
-1

5
1 2 3 -2 -1
-1

5
1 -2 2 -3 2
1
"""
 
def equilibrium(arr): 
	leftsum = 0
	rightsum = 0
	n = len(arr) 
	for i in range(n): 
		leftsum = 0
		rightsum = 0
		for j in range(i): 
			leftsum += arr[j] 
		for j in range(i + 1, n): 
			rightsum += arr[j] 
 
		if leftsum == rightsum: 
			return i 
	return -1
			
N=int(input()) 
arr = list(map(int,input().split()))
print (equilibrium(arr))  
