"""
Question
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.

Input description
First line has integers in list
Second line has the sum 

Output description
print yes or no

Explanation
There is a subset (4, 5) with sum 9.

Input
1 2 3 4 5
9
Output
yes

Input
2 3 1 4 5
4
Output
yes

Input
3 4 5 2
1
Output
no

Input
3 34 4 12 5 2
30
Output
no

Input
1 2
3
Output
yes

Hint
Check if there is any set which sum is equal to sum.
"""
def isSubsetSum(set, n, sum) :
	if (sum == 0) : 
		return True
	if (n == 0 and sum != 0) : 
		return False
	if (set[n - 1] > sum) : 
		return isSubsetSum(set, n - 1, sum);
	return isSubsetSum( 
set, n-1, sum) or isSubsetSum( 
set, n-1, sum-set[n-1]) 
set = list(map(int,input().split()))
sum = int(input())
n = len(set) 
if (isSubsetSum(set, n, sum) == True) : 
	print("yes") 
else : 
	print("no")  
