"""
Given an array A of size N, the task is to check if the given array represents a Binary Max Heap.

In des
The first line of input contains an integer N denoting the size of the array.
Then in the next line are N space separated array elements.

Ot des
If array represents a Binary Max Heap, print "1", else print "0" (without quotes).

6
90 15 10 7 12 2

1

6
9 15 10 7 12 11

0

Exp
From sample
Array of first elements represents Binary Max Heap, so output is 1.

Hint
A Simple Solution is to first check root if it’s greater than all of its descendants. Then check for children of the root.
H 7
T 2500

"""
def isHeap(arr, i, n): 

	if i > int((n - 2) / 2): 
		return True
	if(arr[i] >= arr[2 * i + 1] and
	arr[i] >= arr[2 * i + 2] and
	isHeap(arr, 2 * i + 1, n) and
	isHeap(arr, 2 * i + 2, n)): 
		return True
	
	return False
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) - 1
if isHeap(arr, 0, n):
    print("1")
else:
    print("0") 
 
