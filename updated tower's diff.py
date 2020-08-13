"""
Given heights of n towers and a value k. We need to either increase or decrease height of every tower by k (only once) where k > 0. The task is to minimize the difference between the heights of the longest and the shortest tower after modifications,find the maximum difference.

Hard 6
T 500
in des
First line contain integer N,size of array.
Second line contain N space separated integers,denotes array elements.
Third line contain integer K,the value to be added with each element.

Ot des
Print the max difference of updated array.

5
1 3 2 5 4
3
4



5
3 4 2 1 7
10
6


7
3 2 1 5 4 6 7
7
6



3
1 3 2
1
1


3
1 15 10
6
5



Explanation : We change 1 to 6, 15 to 
9 and 10 to 4. Maximum difference is 5
(between 4 and 9). We can't get a lower
difference.

Hint
The idea is to sort all elements increasing order. And for all elements check if subtract(element-k) and add(element+k) makes any changes or not.

"""
def getMinDiff(arr, n, k): 

	if (n == 1): 
		return 0
 
	arr.sort() 

	ans = arr[n-1] - arr[0] 

	small = arr[0] + k 
	big = arr[n-1] - k 
	
	if (small > big): 
		small, big = big, small 

	for i in range(1, n-1): 
	
		subtract = arr[i] - k 
		add = arr[i] + k 
		if (subtract >= small or add <= big): 
			continue

		if (big - subtract <= add - small): 
			small = subtract 
		else: 
			big = add 
	

	return min(ans, big - small) 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr) 
k = int(input())

print(getMinDiff(arr, n, k)) 

