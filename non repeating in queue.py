"""
Given a stream of characters and we have to find first non repeating character each time a character is inserted to the stream.

H 7
T 2000

Tag queue,yahoo

In des
First line contains integer N,denotes length of string.
Second line contains string of length N.

Ot des
Print space separated non repeating character.
4
aabc

a -1 b b

6
abcabb

a a a b c c 

5
acsac

a a a c s

3
abc

a a a

3
a a c

a -1 c

Exp
From sample:
a -1 b b is the created queue from string with first non repeating character.

Hint
Store each character in queue and increase its frequency in the hash array.For every character of stream, we check front of the queue.If the frequency of character at the front of queue is one, then that will be the first non repeating character.Else if frequency is more than 1, then we pop that element.If queue became empty that means there are no non repeating character so we will print -1.

""" 
from queue import Queue 
def firstnonrepeating(Str): 
	global MAX_CHAR 
	q = Queue() 
	charCount = [0] * MAX_CHAR 
	for i in range(len(Str)): 
		q.put(Str[i])  
		charCount[ord(Str[i]) - ord('a')] += 1
		while (not q.empty()): 
			if (charCount[ord(q.queue[0]) - ord('a')] > 1): 
				q.get() 
			else: 
				print(q.queue[0], end = " ") 
				break

		if (q.empty()): 
			print(-1, end = " ") 
	print() 


MAX_CHAR = 26
n=int(input())
Str = input()
firstnonrepeating(Str) 
