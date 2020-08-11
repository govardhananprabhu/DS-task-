"""
We have to paint n boards of length {A1, A2…An}. There are k painters available and each takes 1 unit time to paint 1 unit of board. The problem is to find the minimum time to get
this job done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.

EXP
Here we can divide the boards into 2
equal sized partitions, so each painter 
gets 20 units of board and the total
time taken is 20.

H
The solution is to consider all possible set of contiguous partitions and calculate the maximum sum partition in each case and return the minimum of all these cases.

Hard 6

T 2000

4
10 10 10 10
2

20


5
10 20 30 40 50
2

90


5
12 34 29 55 44
3

75


3
1 4 2
1

7


4
2 1 4 3
3

4






"""
def sum(arr, frm, to): 
	total = 0; 
	for i in range(frm, to + 1): 
		total += arr[i] 
	return total 
def partition(arr, n, k): 
	if k == 1: 
		return sum(arr, 0, n - 1) 
	if n == 1: 
		return arr[0] 
	best = 100000000

	for i in range(1, n + 1): 
		best = min(best, 
			max(partition(arr, i, k - 1), 
						sum(arr, i, n - 1))) 
	return best
N=int(input())
arr =  list(map(int,input().split()))
n = len(arr) 
k = int(input())
print(partition(arr, n, k)) 

