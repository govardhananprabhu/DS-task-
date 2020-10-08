"""
You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.

H 4 T 1000
Tag Accolite array

In des
First line contains integer N, denotes size of array.
Second line contains N space separated integers denotes array elements.

Ot des
Print the modified array

5
1 1 0 1 0
0 0 1 1 1

4
0 0 0 0
0 0 0 0

3
1 0 1
0 1 1

6
1 1 1 0 1 0
0 0 1 1 1 1

8
1 0 0 0 1 1 1 0
0 0 0 0 1 1 1 1

Exp
First print the number of zeroes and then print number of 1s.

Hint
Count the number of 0s. Let count be C.Once we have count, we can put C 0s at the beginning and 1s at the remaining n – C positions in array.

"""
def segregate0and1(arr, n) :  
	count = 0

	for i in range(0, n) : 
		if (arr[i] == 0) : 
			count = count + 1
	for i in range(0, count) : 
		arr[i] = 0 
	for i in range(count, n) : 
		arr[i] = 1

def print_arr(arr , n) : 

	for i in range(0, n) : 
		print(arr[i] , end = " ") 

N=int(input())

arr = list(map(int,input().split())) 
n = len(arr) 
	
segregate0and1(arr, n) 
print_arr(arr, n) 
