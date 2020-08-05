"""

Given an array of size N and a value, find if there is a providers in array whose
sum is equal to the given value. If there is such a providers present in array,
then print the providers else -1.
Note: providers are any 3 elements in array whose sum is equal to the given value.
I des
First line has size of array N
Second line has array elements
Third line has sum

O des
print providers else -1

Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
Output: 12, 3, 9
Explanation: providers (12, 3 and 9) present
in the array whose sum is 24. 

I
5
1 2 3 4 5
5
O
-1

I
5
1 2 3 4 5
6
O
1 2 3


I
3
1 4 2
7
O
1 4 2

I
1
1
1
O
-1

I
6
12 3 4 1 6 9
24
O
12 3 9
T 900

Hint
A simple method is to generate all possible subarray of len 3 and compare the sum of every triplet with the given value.

""" 
def find3Numbers(A, arr_size, sum): 
	for i in range( 0, arr_size-2):  
		for j in range(i + 1, arr_size-1): 
			for k in range(j + 1, arr_size): 
				if A[i] + A[j] + A[k] == sum: 
					print(A[i], A[j], A[k]) 
					return True
	return False
N=int(input())
A = list(map(int,input().split()))
sum = int(input()) 
if(find3Numbers(A, N, sum)):
    print(end="")
else:
    print(-1)

