"""
Given a number n, print following a pattern without using any loop.

H 5 T 1000
Tag rec

In des
First line contains only one integer N.

Ot des
Print the series

16
16 11 6 1 -4 1 6 11 16

10
10 5 0 5 10

4
4 -1 4

1
1 -4 1

17
17 12 7 2 -3 2 7 12 17
Exp
It basically first reduce 5 one by one until we reach a negative or 0. After we reach 0 or negative, we one add 5 until we reach n.

Hint
The idea is to use recursion.

""" 
def printPattern(n, m, flag):  
	print(m,end=" ") 
	if flag == False and n == m: 
		return
	if flag: 
		if m - 5 > 0: 
			printPattern(n, m - 5, True) 
		else: 
			printPattern(n, m - 5, False) 
	else: 
		printPattern(n, m + 5, False) 

n = int(input())
printPattern(n, n, True) 

# This code is contributed 
# by HrushikeshChoudhary 
