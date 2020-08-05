"""
You are given an unsorted array with both positive and negative elements.
You have to find the smallest positive number missing from the
array. You can modify the original array.

Input des
First line has size of array N
Second line has array elements
Output des
Print the smallest positive number

Exp
Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1


I
8
2 3 7 6 8 -1 -10 15
O
1

I
1
1
O
2

I
3
-1 2 3
O
1

I
5
1 2 3 4 5
O
6

I
12
1 2 3 4 5 6 8 9 10 11 13 -1
O
7

T=700
Hint
We can sort the array in O(nLogn) time. Once the array is sorted,
then all we need to do is a linear scan of the array.
So this approach takes O(nLogn + n) time which is O(nLogn).

"""
def segregate(arr, size): 
	j = 0
	for i in range(size): 
		if (arr[i] <= 0): 
			arr[i], arr[j] = arr[j], arr[i] 
			j += 1
	return j 

def findMissingPositive(arr, size):  
	for i in range(size): 
		if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 
			arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1] 
	for i in range(size): 
		if (arr[i] > 0):  
			return i + 1
	return size + 1

def findMissing(arr, size):
	shift = segregate(arr, size)
	return findMissingPositive(arr[shift:], size - shift) 
N=int(input())
arr = list(map(int,input().split()))
missing = findMissing(arr, N) 
print(missing) 
