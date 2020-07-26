"""
Question
Thanos use his power for every contiguous subarray of size k,find the max power for
every subarray.

Input description
First line has list of integers
second line has integer k

Output description
Print the max power for every subarray.

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3 
Output: 3 3 4 5 5 5 6
Explanation: 
Maximum of 1, 2, 3 is 3
Maximum of 2, 3, 1 is 3
Maximum of 3, 1, 4 is 4
Maximum of 1, 4, 5 is 5
Maximum of 4, 5, 2 is 5 
Maximum of 5, 2, 3 is 5
Maximum of 2, 3, 6 is 6

Input
1 2 3 4 5
3
Output
3 4 5

Input
2 3 4 4 3 6 7 5 2
5
Output
4 6 7 7 7

Input
1 3 5 6 7
2
Output
3 5 6 7

Hint
The idea is very basic run a nested loop, the outer loop which will mark the starting point of
the subarray of length k, the inner loop will run from the starting index to index+k, k
elements from starting index and print the maximum element among these k elements.
Solution:"""
def printMax(arr, n, k): 
	max = 0
	
	for i in range(n - k + 1): 
		max = arr[i] 
		for j in range(1, k): 
			if arr[i + j] > max: 
				max = arr[i + j] 
		print(str(max) + " ", end = "") 

if __name__=="__main__": 
	arr = list(map(int,input().split()))
	n = len(arr) 
	k = int(input())
	printMax(arr, n, k) 

# This code is contributed by Shiv Shankar 
