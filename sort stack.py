"""
Given a stack, the task is to sort it such that the top of the stack has the greatest element.

H 7
T 2500
Tag Yahoo stak

In des
First line contains integer N,denotes size of stack
Second line contains N space separated integers, denotes stack elements

Ot des
Print the stack after the sort

5
11 2 32 3 41

41 32 11 3 2

3
3 2 1

3 2 1

5
-3 14 18 -5 30

30 18 14 -3 -5

3
1 2 3
3 2 1

2
-30 30

30 -30
Exp
Your task is to complete the function sort() which sorts the elements present in the given stack.

Hint
The idea of the solution is to hold all values in Function Call Stack until the stack becomes empty. When the stack becomes empty, insert all held items one by one in sorted order.


""" 
def sortedInsert(s , element): 
	if len(s) == 0 or element > s[-1]: 
		s.append(element) 
		return
	else: 
		temp = s.pop() 
		sortedInsert(s, element) 
		s.append(temp) 
def sortStack(s): 
	if len(s) != 0:  
		temp = s.pop() 
		sortStack(s)  
		sortedInsert(s , temp) 
def printStack(s): 
	for i in s[::-1]: 
			print(i , end=" ") 
	print() 
n=int(input())	
s=list(map(int,input().split()))
sortStack(s)
printStack(s) 


