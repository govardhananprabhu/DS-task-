"""
You will be given two arrays A and B of positive integers. The number of values in both the arrays will be the same say N. Your task is to find the maximum sum of products of their elements. Each element in A has to be multiplied with exactly one element in B and vice versa such that each element of both the arrays appears exactly once and the sum of product produced is maximum.

In des
The first line consists of N the size of the two arrays.
In the next line N space separated positive integers denoting the values in array A and in the third line are N space separated positive integers denoting the values in array B.

Ot des
Print the maximum possible sum of products of the elements.

5
5 1 3 4 2
8 10 9 7 6

130

3
1 2 3
4 5 1

24

6
1 3 5 6 8 9
12 34 55 12 11 10
942

4
1 2 3 4
1 2 3 4
30

1
1
1
1

Exp
if A = {5,1,3,4,2} and B = {8,10,9,7,6} then a possible sum of product is 5*6 + 1*7 + 3*9 + 4*10 + 2*8.
output=130

Hint
Sort both the arrays.
Traverse the arrays, and calculate the sum of products of array elements that are at the same index.

H 5
T 2000

Accolite array sort

""" 
def maximumSOP(a, b) : 
	sop = 0 
	n = len(a) 
	a.sort() 
	b.sort() 
	for i in range(n) : 
		sop += a[i] * b[i] 

	return sop
N=int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(maximumSOP(A, B)) 
