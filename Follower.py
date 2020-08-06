"""
A1 is the fallower of A2,help A1 to fallow A2.
Given two arrays A1[] and A2[], sort A1 in such a way that the relative order among
the elements will be same as those are in A2. For the elements not present in A2,
append them at last in sorted order.

in des
First line contain space separated integers a1,a2,which denotes the size of two arrays
Second line contain a1 space separated integers
Third line contain a2 space separated integers

Out des
Print the sorted array

Explanation
From sample
In a2 array first element is 2 which is present in a1,so it comes first.
similarly 2 2 1 1 8 8 3 after these elements print the rest of the elements in sorted order
2 2 1 1 8 8 35 6 7 9.

Hint
Make the first element in a2 is the first in a1,and so on till last element in a2,
then sort the remaining elements.
In
11 4
2 1 2 5 7 1 9 3 6 8 8
2 1 8 3
Ot
2 2 1 1 8 8 3 5 6 7 9

In
3 2
1 2 3
1 3
Ot
1 3 2


In
4 5
1 2 3 4
3 2 6 5 1
Ot
3 2 1 4


In
5 5
1 2 3 4 5
5 4 3 2 1
Ot
5 4 3 2 1


In
1 1
1
1
Ot
1

T 1200

"""


def first(arr, low, high, x, n) : 
	if (high >= low) : 
		mid = low + (high - low) // 2; 
		if ((mid == 0 or x > arr[mid-1]) and arr[mid] == x) : 
			return mid 
		if (x > arr[mid]) : 
			return first(arr, (mid + 1), high, x, n) 
		return first(arr, low, (mid -1), x, n) 
		
	return -1
 
def sortAccording(A1, A2, m, n) : 

	temp = [0] * m 
	visited = [0] * m 
	
	for i in range(0, m) : 
		temp[i] = A1[i] 
		visited[i] = 0


	temp.sort() 

	ind = 0	

	for i in range(0, n) : 
 
		f = first(temp, 0, m-1, A2[i], m) 
		if (f == -1) : 
			continue

		j = f 
		while (j<m and temp[j]== A2[i]) : 
			A1[ind] = temp[j]; 
			ind = ind + 1
			visited[j] = 1
			j = j + 1
	 
	for i in range(0, m) : 
		if (visited[i] == 0) : 
			A1[ind] = temp[i] 
			ind = ind + 1
			
def printArray(arr, n) : 
	for i in range(0, n) : 
		print(arr[i], end = " ") 
	print("") 
	
a1,a2= map(int,input().split())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))
m = len(A1) 
n = len(A2) 
sortAccording(A1, A2, m, n) 
printArray(A1, m) 


