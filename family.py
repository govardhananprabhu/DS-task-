"""
Given an array of integers you have to find three numbers such that sum of two
elements equals the third element.

In des
First line size of array N
Second line has array elements

Out des
print the family else -1

Exp
Input : {5, 32, 1, 7, 10, 50, 19, 21, 2}
Output : 21, 2, 19
19+2=21


I
3
1 2 4
O
-1

I
3
1 3 4
O
4 1 3


I
9
5 32 1 7 10 50 19 21 2
O
21 2 19

I
3
1 2 3
O
3 1 2

I
12
1 2 3 4 5 6 8 9 10 11 13 -1
O
13 2 11

T 2500

Hint

Run three loops and check if there exists a triplet such that sum of two
elements equals the third element.
""" 
def findTriplet(arr, n): 
	arr.sort()  
	i = n - 1
	while(i >= 0): 
		j = 0
		k = i - 1
		while (j < k): 
			if (arr[i] == arr[j] + arr[k]): 
				print(arr[i], arr[j], arr[k]) 
				return
			elif (arr[i] > arr[j] + arr[k]): 
				j += 1
			else: 
				k -= 1
		i -= 1
		
	
	print(-1)
N=int(input())
arr = list(map(int,input().split())) 
findTriplet(arr, N) 
 
