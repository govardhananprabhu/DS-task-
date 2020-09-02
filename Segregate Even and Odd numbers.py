"""
Given an array A[], write a program that segregates even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

In des
The first line contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Ot des
print the segregated array.

7
12 34 45 9 8 90 3

8 12 34 90 3 9 45

5
0 1 2 3 4

0 2 4 1 3

3
1 4 2
2 4 1

2
2 1
2 1

5
1 2 43 5 22
22 2 43 5 1

From sample:
In the output, the order of numbers can be changed 34 can come before 12 and 3 can come before 9.

Hint
Initialize two index variables left and right:left = 0,  right = size -1.Keep incrementing left index until we see an odd number.Keep decrementing right index until we see an even number.If lef < right then swap arr[left] and arr[right].

H 6
T 2000

Accolite array sorting

"""
def segregateEvenOdd(arr): 
	left,right = 0,len(arr)-1

	while left < right:  
		while (arr[left]%2==0 and left < right): 
			left += 1
		while (arr[right]%2 == 1 and left < right): 
			right -= 1

		if (left < right): 
			arr[left],arr[right] = arr[right],arr[left] 
			left += 1
			right = right-1
N=int(input())
arr = list(map(int,input().split()))
segregateEvenOdd(arr) 
print(*arr)
