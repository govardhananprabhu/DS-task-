"""
Given a string S consisting of lowercase Latin letters, arrange all its letters in lexicographical order using Counting Sort.

H 6
T 2000

In des
First line contain integer N,denotes length of string.
Second line contains string of length N

Ot des
Print the sorted string

Tag cico string
5
edsab

abdes

11
explanation

aaeilnnoptx

3
cat
act

3
sad
ads

5
water
aertw

Explanation:
From sample:
In lexicographical order, string will be abdes.

Hint
First consider the count array of 256,then by using ASCII vaue assign the count of each character in count array,then print the sorted string by created count array.

""" 
def countSort(arr): 
	output = [0 for i in range(len(arr))] 
	count = [0 for i in range(256)] 

	ans = ["" for _ in arr] 
	for i in arr: 
		count[ord(i)] += 1
	for i in range(256): 
		count[i] += count[i-1]  
	for i in range(len(arr)): 
		output[count[ord(arr[i])]-1] = arr[i] 
		count[ord(arr[i])] -= 1 
	for i in range(len(arr)): 
		ans[i] = output[i] 
	return ans 
N=int(input())
arr = input()
ans = countSort(arr) 
print(("".join(ans))) 
