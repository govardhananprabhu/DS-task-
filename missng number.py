"""
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

In des
First line contain integer N,size of array.
Second line contain N space separated integers,denotes array elements.

Ot description
Print the missing number

7
1 2 4 6 3 7 8

5

4
1 2 3 5

4


Exp
From sample
The missing number from 1 to 8 is 5

Hint
The length of the array is n-1. So the sum of all n elements, i.e sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. Now find the sum of all the elements in the array and subtract it from the sum of first n natural numbers, it will be the value of the missing element.

H 6
T 2000

"""
def getMissingNo(A): 
	n = len(A) 
	total = (n + 1)*(n + 2)/2
	sum_of_A = sum(A) 
	return total - sum_of_A 
N=int(input())
A = list(map(int,input().split()))
miss = getMissingNo(A) 
print(miss)
