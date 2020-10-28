"""
Given an array of integers (both odd and even), the task is to arrange them in such a way that odd and even values come in alternate fashion in non-decreasing order(ascending) respectively.

If the smallest value is Even then we have to print Even-Odd pattern.
If the smallest value is Odd then we have to print Odd-Even pattern.

H 5 T 1000
Tag array

In des
First line contains integer N, size of array.
Second line contains N space separated integers, denotes array elements.
Ot des
print the altered array

7
1 3 2 5 4 7 10

1 2 3 4 5 10 7

6
9 8 13 2 19 14

2 9 8 13 14 19

5
4 2 5 3 8
2 3 4 5 8 

3
1 3 2
1 2 3

4
2 1 3 5
1 2 3 5
Exp
Smallest value is 1(Odd) so output will be Odd-Even pattern.

Hint
find the samllest element and order according to it
"""

def AlternateRearrange(arr, n): 

	arr.sort() 

	v1 = list() 
	v2 = list() 

	for i in range(n): 
		if (arr[i] % 2 == 0): 
			v1.append(arr[i]) 
		else: 
			v2.append(arr[i]) 

	index = 0
	i = 0
	j = 0

	flag = False

	if (arr[0] % 2 == 0): 
		flag = True


	while (index < n): 

		if (flag == True): 
			arr[index] = v1[i] 
			index += 1
			i += 1
			flag = ~flag 
		
	
		else: 
			arr[index] = v2[j] 
			index += 1
			j += 1

			flag = ~flag 
		
	for i in range(n): 
		print(arr[i], end = " ") 


n=int(input())
arr = list(map(int,input().split()))
AlternateRearrange(arr, n) 

