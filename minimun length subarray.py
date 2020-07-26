"""Question
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

Input description
First line has integers in list
second line has X interger

Output description
Print the length else print Not possibe

Explanation:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}


Solution"""
def smallestSubWithSum(arr, n, x): 

 
	min_len = n + 1


	for start in range(0,n): 
 
		curr_sum = arr[start] 

	
		if (curr_sum > x): 
			return 1

		for end in range(start+1,n): 
			curr_sum += arr[end] 
 
			if curr_sum > x and (end - start + 1) < min_len: 
				min_len = (end - start + 1) 
		
	return min_len; 

arr1 = list(map(int,input().split())) 
x = int(input())
n1 = len(arr1) 
res1 = smallestSubWithSum(arr1, n1, x); 
if res1 == n1+1: 
	print("Not possible") 
else: 
	print(res1) 

