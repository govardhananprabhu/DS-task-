"""
There is an array contains N number of patients in hospital ,the task is to find the Kth strongest person in it. 

H 4 T cisco
T 1000

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers ,denotes array elements.
Third line contains integer K ,denotes kth person.

Ot
Print the Kth strongest person.

Exp
10 is the 3rd weakest person in hospital

6
7 10 4 3 20 15
3
10

6
7 10 4 3 20 15
4
7

4
2 1 4 3
2
3

7
12 44 135 45 1121 1789 76
4
76

6
7 10 4 3 20 15
6
20

Hint
Sort the array and print the Kth element of array

"""
def kthSmallest(arr, l, r, k): 
	if (k > 0 and k <= r - l + 1): 

		n = r - l + 1

		median = [] 

		i = 0
		while (i < n // 5): 
			median.append(findMedian(arr, l + i * 5, 5)) 
			i += 1 
		if (i * 5 < n): 
			median.append(findMedian(arr, l + i * 5, 
											n % 5)) 
			i += 1
		if i == 1: 
			medOfMed = median[i - 1] 
		else: 
			medOfMed = kthSmallest(median, 0, i - 1, i // 2) 

		pos = partition(arr, l, r, medOfMed)  
		if (pos - l == k - 1): 
			return arr[pos] 
		if (pos - l > k - 1): 
			return kthSmallest(arr, l, pos - 1, k) 
		return kthSmallest(arr, pos + 1, r, k - pos + l - 1) 
 
	return 999999999999

def swap(arr, a, b): 
	temp = arr[a] 
	arr[a] = arr[b] 
	arr[b] = temp  
def partition(arr, l, r, x): 
	for i in range(l, r): 
		if arr[i] == x: 
			swap(arr, r, i) 
			break

	x = arr[r] 
	i = l 
	for j in range(l, r): 
		if (arr[j] <= x): 
			swap(arr, i, j) 
			i += 1
	swap(arr, i, r) 
	return i 
def findMedian(arr, l, n): 
	lis = [] 
	for i in range(l, l + n): 
		lis.append(arr[i]) 
	lis.sort() 
	return lis[n // 2] 
N=int(input())
arr = list(map(int,input().split()))
n = len(arr)
k = int(input())
print(kthSmallest(arr, 0, n - 1, k)) 
