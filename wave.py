"""
Question
Given an unsorted array of integers, sort the array into a wave like array. An array
‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

Input description
First line has integer N
Second line has list of integers
Output description
Print the array in wave form
Explanation
 Input:  arr[] = {3, 6, 5, 10, 7, 20}
 Output: arr[] = {6, 3, 10, 5, 20, 7} OR
                 any other array that is in wave form
Input
5
1 2 3 4 5
Output
2 1 4 3 5

Input
5
3 2 4 5 6
Output
3 2 5 4 6

Input
8
3 2 4 5 6 7 1 2
Output
2 1 3 2 5 4 7 6

Input
8
22 3 1 4 5 55 44 9
Output
3 1 5 4 22 9 55 44

Input
4
1 3 2 4
Output
2 1 4 3
Hint
A Simple Solution is to use sorting. First sort the input array, then swap all adjacent elements.
Solution"""
def sortInWave(arr, n): 
	arr.sort() 
	for i in range(0,n-1,2): 
		arr[i], arr[i+1] = arr[i+1], arr[i]
N=int(input())
arr = list(map(int,input().split()))
sortInWave(arr, len(arr)) 
for i in range(0,len(arr)): 
	print(arr[i],end=" ") 
