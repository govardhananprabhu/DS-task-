"""
Given an array representing heights of towers. The array has buildings from left to right,count number of pillars facing the sunset. It is assumed that heights of all pillars are distinct.

H 6 T 1000
Tag array

In des
First line contains integer N, denotes size of array.
Second line contains N space separated integers, denotes array elements.

Ot des
Print the count

5
7 4 8 2 9
3

4
2 3 4 5
4

5
1 2 3 4 0
4

4
3 4 2 7
3

7
4 7 3 55 3 2 98
4
Exp
As 7 is the first element, it can 
see the sunset.
4 can't see the sunset as 7 is hiding it. 
8 can see.
2 can't see the sunset.
9 also can see the sunset

Hint
It can be easily observed that only the maximum element found so far will see the sunlight
"""
def countBuildings(arr, n): 
	count = 1 
	curr_max = arr[0] 
	for i in range(1, n):  
		if (arr[i] > curr_max): 
		
			count += 1
			curr_max = arr[i] 

	return count 
n=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
print(countBuildings(arr, n)) 

# This code is contributed by Anant Agarwal. 
