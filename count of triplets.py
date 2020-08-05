"""
Given an array A[] of N integers. The task is to find the number of triples
(i, j, k) , where i, j, k are indices and (1 <= i < j < k <= N), such that in the
set { A_i, A_j, A_k} at least one of the numbers can be written as the sum of the
other two.

In des
First line has size of array N
Second line has array elements

Out des
Print the count of triplets

Exp
Input : A[] = {1, 2, 3, 4, 5}
Output : 4
The valid triplets are:
(1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)

I
5
1 2 3 4 5
O
4

I
6
3 2 1 4 5 7
O
6

I
4
11 2 8 5
O
0

I
1
1
O
0


I
4
1 1 1 3
O
0

T 1000


Hint
First find the possible triplets,then check sum of two gives the third element if yes
count it,print the count after checking all possibilities.
"""
import math as mt 

def countWays(arr, n): 
	max_val = 0
	for i in range(n): 
		max_val = max(max_val, arr[i]) 

	freq = [0 for i in range(max_val + 1)] 

	for i in range(n): 
		freq[arr[i]] += 1

	ans = 0 
	ans += (freq[0] * (freq[0] - 1) *
		(freq[0] - 2) // 6) 
 
	for i in range(1, max_val + 1): 
		ans += (freq[0] * freq[i] *
			(freq[i] - 1) // 2) 

	for i in range(1, (max_val + 1) // 2): 
		ans += (freq[i] *
			(freq[i] - 1) // 2 * freq[2 * i]) 
 
	for i in range(1, max_val + 1): 
		for j in range(i + 1, max_val - i + 1): 
			ans += freq[i] * freq[j] * freq[i + j] 

	return ans 

N=int(input())
arr = list(map(int,input().split())) 
n = len(arr) 
print(countWays(arr, n)) 
