"""
Question
Avengers need to destroy ultran but there is some logic to solve,Ultran is an AI machine
Tony Stark founded that there is a weakness,he found an array it has both positive
and negative integers,if they are able to find the sum of integers is equal to 0
but the count of integer used for sum should be greater than 3,if not print -1.

Input description
First line has list of integers

Output description
print the count or -1

Explanation
1 2 3 -3 -2 -1
1+2+3-3-2-1=0
count=6

Input
1 2 3 0 1
Output
-1

Input
1 -2 1 0
Output
4

Input
0 0 0 0 0 0
Output
6

Input
6 -1 -2 -3 -4 -5 -6
Output
4

Input
0
Output
-1

Hint
Consider all sub-arrays one by one and check the sum of every sub-array.
Run two loops: the outer loop picks the starting point i and the inner loop tries all sub-arrays starting from i.
Solution:"""
def maxLen(arr):
	max_len = 0
	for i in range(len(arr)): 
		curr_sum = 0
		
		for j in range(i, len(arr)): 
		
			curr_sum += arr[j] 
 
			if curr_sum == 0: 
				max_len = max(max_len, j-i + 1) 

	return max_len 



arr = list(map(int,input().split()))

if(maxLen(arr)>3):
    print(maxLen(arr))
else:
    print(-1)
