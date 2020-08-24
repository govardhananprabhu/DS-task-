"""
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes array elements.

Ot des
Print the sum

4
3 2 7 10

13

5
3 2 5 10 7

15

6
5 5 10 100 10 5

110

3
1 2 3

4

3
1 20 3

20

Exp
From sample,
So 3 2 7 10 should return 13 (sum of 3 and 10).

Hint
Traverse the array and for each element add it with the non adjacent greater number,updtae if the next sum value is greater,finally print the sum. 

H 6
T 2500
"""
def find_max_sum(arr): 
	incl = 0
	excl = 0
	
	for i in arr: 

		new_excl = excl if excl>incl else incl  
		incl = excl + i 
		excl = new_excl 
	return (excl if excl>incl else incl) 

N=int(input())
arr = list(map(int,input().split()))
print(find_max_sum(arr)) 
