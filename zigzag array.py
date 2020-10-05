"""
The longest Zig-Zag subsequence problem is to find length of the longest subsequence of given sequence such that all elements of this are alternating.

H 7
T 2000
Tag accolite array

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers, denotes array elements.

Ot des
Print the length of zigzag.

3
1 5 4

3

3
1 4 5
2

8
10 22 9 33 49 50 31 60
6

5
1 4 2 5 6
4

6
1 2 5 3 4 9
4

Exp
The whole arrays is of the form  x1 < x2 > x3 

Hint
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy one of the following relation :
x1 < x2 > x3 < x4 > x5 < …. xn or 
x1 > x2 < x3 > x4 < x5 > …. xn 
""" 
def zzis(arr, n): 
	Z = [[1 for i in range(2)] for i in range(n)] 


	res = 1  
	for i in range(1, n): 
		for j in range(i): 
			if (arr[j] < arr[i] and Z[i][0] < Z[j][1] + 1): 
				Z[i][0] = Z[j][1] + 1 
			if( arr[j] > arr[i] and Z[i][1] < Z[j][0] + 1): 
				Z[i][1] = Z[j][0] + 1
		if (res < max(Z[i][0], Z[i][1])): 
			res = max(Z[i][0], Z[i][1]) 

	return res 
N=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
print(zzis(arr, N)) 

