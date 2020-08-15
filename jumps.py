"""
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, they cannot move through that element.
In des
First line contain integer N,sizre of array.
Second line contain N space separated integers, denotes array elements.

Ot des
Print min jumps



11
1 3 5 8 9 2 6 7 6 8 9
3

11
1 1 1 1 1 1 1 1 1 1 1
10

Exp
From sample
Jump from 1st element 
to 2nd element as there is only 1 step, 
now there are three options 5, 8 or 9. 
If 8 or 9 is chosen then the end node 9 
can be reached. So 3 jumps are made.


Hint
To start from the first element and recursively call for all the elements reachable from first element. The minimum number of jumps to reach end from first can be calculated using minimum number of jumps needed to reach end from the elements reachable from first.
H 6
T 2000
"""
def minJumps(arr, l, h):  
	if (h == l): 
		return 0
 
	if (arr[l] == 0): 
		return float('inf')  
	min = float('inf') 
	for i in range(l + 1, h + 1): 
		if (i < l + arr[l] + 1): 
			jumps = minJumps(arr, i, h) 
			if (jumps != float('inf') and
					jumps + 1 < min): 
				min = jumps + 1

	return min

N=int(input()) 
arr = list(map(int,input().split()))
n = len(arr) 
print(minJumps(arr, 0, n-1)) 

# This code is contributed by Soumen Ghosh 
