"""
Question
Thanos put his powers in unsorted array of nonnegative integers,he wants it back but he
not have the knowledge of subarray,he asks you to help by finding the continuous subbary's
sum equal's to his power if not print -1.

Input description
First line has integers in list
Second line has power in integer

Output description
print the range(index)

Explanation:
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33

Input
1 2 3 4
5
Output
1 2

Input
1 2 3 4 5 6 7
0
Output
-1

Input
2 33 4 55 66 1
92
Output
1 3

Input
1 2 3 4 5 6
22
Output
-1

Input
1
1
Output
0

Hint

Traverse the array from start to end.
From every index start another loop from i to the end of array to get all subarray starting from i, keep a varibale sum to calculate the sum.
For every index in inner loop update sum = sum + array[j]
If the sum is equal to the given sum then print the subarray.

Solution:"""
def subArraySum(arr, n, sum): 
 
	for i in range(n): 
		curr_sum = arr[i] 

		j = i + 1
		while j <= n: 
		
			if curr_sum == sum: 
				print(i, j-1) 
				
				return 1
				
			if curr_sum > sum or j == n: 
				break
			
			curr_sum = curr_sum + arr[j] 
			j += 1

	print ("-1") 
	return 0
arr = list(map(int,input().split()))
n = len(arr) 
sum = int(input())

subArraySum(arr, n, sum) 
