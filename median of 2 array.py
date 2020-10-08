"""
There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n).

H 6
T 2000
Tag accolite array

In des
First line contains integer N, denotes size of a arrays.
Second and third line contains N space separated integers, denotes arr1 and arr2.

Ot des
Print the median else unequal size.

5
1 12 15 26 38
2 13 17 30 45

16

5
1 12 15 26 38
2 13 17 30

unequal size

3
1 3 2
4 3 2

3

4
1 2 3 4
4 3 2 1

4

4
1 2 3 4
4
unequal size
Exp
From sample
after merging 1 2 12 13 15 17 26 30 38 45 find its median
(15+17)/2=16
Hint
Use the merge procedure of merge sort. Keep track of count while comparing elements of two arrays. If count becomes n(For 2n elements), we have reached the median. Take the average of the elements at indexes n-1 and n in the merged array. See the below implementation.
"""
def getMedian( ar1, ar2 , n):
	i = 0 
	
	j = 0 
	
	m1 = -1
	m2 = -1
	count = 0
	while count < n + 1:
		count += 1
		
		if i == n:
			m1 = m2
			m2 = ar2[0]
			break

		elif j == n:
			m1 = m2
			m2 = ar1[0]
			break
 
		if ar1[i] <= ar2[j]:
			m1 = m2 
			m2 = ar1[i]
			i += 1
		else:
			m1 = m2 
			m2 = ar2[j]
			j += 1
	return (m1 + m2)/2
N=int(input())
ar1=list(map(int,input().split()))
ar2=list(map(int,input().split()))
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
	print(int(getMedian(ar1, ar2, n1)))
else:
	print("unequal size")

