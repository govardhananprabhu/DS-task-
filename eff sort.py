"""
Given two sorted arrays, we need to merge them in O((n+m)*log(n+m)) time with O(1) extra space into a sorted array, when n is the size of the first array, and m is the size of the second array.

H 8 2000
Tag array sort

In des
First line contains 2 integers n, m, denotes size of arrays.
Second line contains n space separated integers, denotes array elements.
Third line contains m space separated integers, denotes array elements.

Ot des
Print both array in sorted order.

1 2
10
2 3

2
3 10

6 4
1 5 9 10 15 20
2 3 8 13

1 2 3 5 8 9
10 13 15 20

2 3
1 4
2 3 1
1 1 
2 3 4

4 5
1 3 2 55 
90 87 66 10
1 2 3 10 
55 66 87 90

4 2
1 33 21 14
9 8
1 8 9 14 
21 33

Exp
sort and arrange by given array size

Hint
We start comparing elements that are far from each other rather than adjacent. 
For every pass, we calculate the gap and compare the elements towards the right of the gap. Every pass, the gap reduces to the ceiling value of dividing by 2.

"""
def nextGap(gap):

	if (gap <= 1):
		return 0
	return (gap // 2) + (gap % 2)


def merge(arr1, arr2, n, m):

	gap = n + m
	gap = nextGap(gap)
	while gap > 0:
		i = 0
		while i + gap < n:
			if (arr1[i] > arr1[i + gap]):
				arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]

			i += 1
		j = gap - n if gap > n else 0
		while i < n and j < m:
			if (arr1[i] > arr2[j]):
				arr1[i], arr2[j] = arr2[j], arr1[i]

			i += 1
			j += 1

		if (j < m):
			j = 0
			while j + gap < m:
				if (arr2[j] > arr2[j + gap]):
					arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]

				j += 1

		gap = nextGap(gap)

a,b=map(int,input().split())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
n = len(a1)
m = len(a2)
merge(a1, a2, n, m)
for i in range(n):
    print(a1[i], end=" ")
print()
for i in range(m):
    print(a2[i], end=" ")
print()
