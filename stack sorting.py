"""
Given a stack of integers, sort it in descending order using another temporary stack.

H 7
T 2000
Tag yahoo stack

In des
First line contains integer N, denotes size of stack
Second line contains N space separated integers, denotes stack elements

Ot des
Print the sorted stack else Stack Underflow 

5
3 1 4 2 5
5 4 3 2 1

4
33 21 43 12
43 33 21 12

7
2 1 5 3 4 6 7
7 6 5 4 3 2 1

3
3 1 2
3 2 1

3
10 09 2
10 9 2

Exp
From sample:
The sorted stack is 5 4 3 2 1
Hint
Create a temporary stack say tmpStack.
While input stack is NOT empty do this:
Pop an element from input stack call it temp
while temporary stack is NOT empty and top of temporary stack is greater than temp,
pop from temporary stack and push it to the input stack
push temp in temporary stack
The sorted numbers are in tmpStack
"""
def sortStack ( stack ): 
	tmpStack = createStack() 
	while(isEmpty(stack) == False):  
		tmp = top(stack) 
		pop(stack) 
		while(isEmpty(tmpStack) == False and
			int(top(tmpStack)) > int(tmp)): 
			push(stack,top(tmpStack)) 
			pop(tmpStack) 
		push(tmpStack,tmp) 
	
	return tmpStack 
def createStack(): 
	stack = [] 
	return stack 
def isEmpty( stack ): 
	return len(stack) == 0
def push( stack, item ): 
	stack.append( item ) 
def top( stack ): 
	p = len(stack) 
	return stack[p-1]  
def pop( stack ): 
	if(isEmpty( stack )): 
		print("Stack Underflow") 
		exit(1) 

	return stack.pop() 

def prints(stack): 
	for i in range(len(stack)-1, -1, -1): 
		print(stack[i], end = ' ') 
	print() 
stack = createStack()
N=int(input())
l=list(map(int,input().split()))
for i in range(N):
    push( stack, str(l[i]) ) 
sortedst = sortStack ( stack ) 
prints(sortedst) 
