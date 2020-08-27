"""
Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.

In des
First line contain integer N,denotes size of array.
Second line contain N space separated integers,denotes array elements.

Ot des
Print the first non repeating character

12
zxvczbtxyzvy

c

6
xxyyzz

-1

5  
hello

h

14
geeksforgeeks
f

Exp
Step 1: Construct a character count array 
        from the input string.
   ....
  count['e'] = 4
  count['f'] = 1
  count['g'] = 2
  count['k'] = 2
  ……

Step 2: Get the first character who's 
        count is 1 ('f').


""" 
NO_OF_CHARS = 256
def getCharCountArray(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)]+= 1
	return count 
 
def firstNonRepeating(string): 
	count = getCharCountArray(string) 
	index = -1
	k = 0

	for i in string: 
		if count[ord(i)] == 1: 
			index = k 
			break
		k += 1

	return index  
N=int(input())
string = input()
index = firstNonRepeating(string) 
if index == 1: 
	print("-1")
else: 
	print(string[index])
