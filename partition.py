"""
Given an integer array of N elements, the task is to divide this array into K non-empty subsets such that the sum of elements in every subset is same. All elements of this array should be part of exactly one partition.
H 6
T 2300
Tag accolite array
In des
First line contain integer N,denotes size of array.
Second line contains N space separated integers, denotes array elements.
Third line contain integer K, denotes the count of sets

Ot des
Print yes if it has K sets else no
5
2 1 4 5 6
3

yes

5
2 1 5 5 6
3

no

6
1 2 3 4 5 6
2
no

4
1 1 1 1
4
yes

3
1 2 3
2
yes

Exp
Yes
we can divide above array into 3 parts with equal
sum as [[2, 4], [1, 5], [6]]

Hint
We can solve this problem recursively, we keep an array for sum of each partition and a boolean array to check whether an element is already taken into some partition or not.

"""
def isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, curIdx, limitIdx): 
	if subsetSum[curIdx] == subset: 
		if (curIdx == K - 2): 
			return True
		return isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, curIdx + 1 , N - 1)  
	for i in range(limitIdx, -1, -1):  
		if (taken[i]): 
			continue
		tmp = subsetSum[curIdx] + arr[i] 
		if (tmp <= subset): 
			taken[i] = True
			subsetSum[curIdx] += arr[i] 
			nxt = isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, curIdx, i - 1) 
			taken[i] = False
			subsetSum[curIdx] -= arr[i] 
			if (nxt): 
				return True
	return False
def isKPartitionPossible(arr, N, K): 
	if (K == 1): 
		return True
	if (N < K): 
		return False 
	sum = 0
	for i in range(N): 
		sum += arr[i] 
	if (sum % K != 0): 
		return False 
	subset = sum // K 
	subsetSum = [0] * K 
	taken = [0] * N  
	for i in range(K): 
		subsetSum[i] = 0
	for i in range(N): 
		taken[i] = False 
	subsetSum[0] = arr[N - 1] 
	taken[N - 1] = True
	return isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, 0, N - 1) 
n=int(input())
arr = list(map(int,input().split())) 
N = len(arr) 
K = int(input())
if (isKPartitionPossible(arr, N, K)): 
	print("yes") 
else: 
	print("no") 
