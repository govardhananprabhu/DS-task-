"""
Write a program to print all permutations of a given string.

In des
First line contain string S.

Ot des
Print all permutation in each line.

ABC

ABC
ACB
BAC
BCA
CBA
CAB

Exp
From sample
There are 6 permutation for the given string,
ABC ACB BAC BCA CBA CAB


Hint
A permutation, also called an “arrangement number” or “order,” is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.

H 7
T 2500

"""
def toString(List): 
	return ''.join(List)  
def permute(a, l, r): 
	if l==r: 
		print(toString(a)) 
	else: 
		for i in range(l,r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l] 
string = input()
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 

