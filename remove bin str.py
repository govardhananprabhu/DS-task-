"""
Given a binary string str, the task is to remove the minimum number of characters from the given binary string such that the characters in the remaining string form a sorted order.

H 5 T 1000
Tag string

In des:
First line contains a single string only.

Ot des
Print the count of removed char.

1000101
2

001111
0

111100000
4

10101000
3

10000001
2

Exp
Removal of the first two occurrences of ‘1’ modifies the string to “00001”, which is a sorted order.
Therefore, the minimum count of characters to be removed is 2.

Hint
The idea is to count the number of 1s before the last occurrence of 0 and the number of 0s before the first occurrence of 1. The minimum of the two counts is the required number of characters to be removed

"""
def minDeletion(s):
	n = len(s)
	firstIdx1 = -1
	lastIdx0 = -1
	for i in range(0, n):
		if (str[i] == '1'):
			firstIdx1 = i
			break 
	for i in range(n - 1, -1, -1):
		if (str[i] == '0'): 
			lastIdx0 = i
			break
	if (firstIdx1 == -1 or
		lastIdx0 == -1):
		return 0 
	count1 = 0
	count0 = 0
	for i in range(0, lastIdx0):
		if (str[i] == '1'): 
			count1 += 1 
	for i in range(firstIdx1 + 1, n):
		if (str[i] == '1'):
			count0 += 1
	return min(count0, count1)+1
str = input()
print(minDeletion(str))
