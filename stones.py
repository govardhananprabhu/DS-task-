"""
Question
Thanos founded three stones but he wants to find the remaining three,tony stark hided
three in array,help thanos to find remaining three.The three is sorted subsequence in
array,if more than one possible of pairs occurs print best pair
example
Input
4
1 2 3 4
Output
1 2 4

Input description
First line has size of array
Second line has array elements(integers)
Output description
Print the stones or "No stones found"

Explanation
Input: arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30
Explanation: As 5 < 6 < 30, and they 
appear in the same sequence in the array 

Input
4
5 2 3 4
Output
2 3 4

Input
5
2 1 6 4 5 
Output
1 4 5

Input
7
12 11 10 5 6 2 30
Output
5 6 30 

Input
4
4 3 2 1
Output
No stones found

Input
4
1 2 3 4
Output
1 2 4
Hint

Solution:"""
def find3numbers(arr): 
	n = len(arr)  
	max = n-1 
	min = 0
	smaller = [0]*10000
	smaller[0] = -1
	for i in range(1, n): 
		if (arr[i] <= arr[min]): 
			min = i 
			smaller[i] = -1
		else: 
			smaller[i] = min
	greater = [0]*10000
	greater[n-1] = -1

	for i in range(n-2, -1, -1): 
		if (arr[i] >= arr[max]): 
			max = i 
			greater[i] = -1

		else: 
			greater[i] = max
	for i in range(0, n): 
		if smaller[i] != -1 and greater[i] != -1: 
			print(arr[smaller[i]], arr[i], arr[greater[i]]) 
			return
	print("No stones found")
	return


N=int(input())
arr = list(map(int,input().split()))
find3numbers(arr) 
