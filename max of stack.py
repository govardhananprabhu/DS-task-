"""
Given a Stack, keep track of the maximum value in it. The maximum value may be the top element of the stack, but once a new element is pushed or an element is popped from the stack, the maximum element will be now from the rest of the elements.

H 7
T 2300
Tag yahoo stack

In des
First line contains integer N,denotes the size of stack.
Second line contains N space separated integers,denotes stack elements.

Ot des
Print space separated max element for each next element.


5
4 19 7 14 20

4 19 19 19 20

6
40 19 7 14 20 5

40 40 40 40 40 40

6
1 2 3 4 5 6

1 2 3 4 5 6

6
6 5 4 3 2 1

6 6 6 6 6 6

3
1 5 3

1 5 5 
Exp
From sample:
Max Values in stack are 4 19 19 19 20

Hint
We keep pushing the elements in the main stack and whenever we are asked to return the maximum element, we traverse the stack and print the max element.
"""
class StackWithMax: 
	def __init__(self): 
		self.mainStack = [] 
		self.trackStack = [] 

	def push(self, x): 
		self.mainStack.append(x) 
		if (len(self.mainStack) == 1): 
			self.trackStack.append(x) 
			return 
		if (x > self.trackStack[-1]): 
			self.trackStack.append(x) 
		else: 
			self.trackStack.append(self.trackStack[-1]) 

	def getMax(self): 
		return self.trackStack[-1] 

	def pop(self): 
		self.mainStack.pop() 
		self.trackStack.pop() 


s = StackWithMax()
N=int(input())
l=list(map(int,input().split()))
for i in l:
    s.push(i)
    print(s.getMax(),end=" ") 
 

