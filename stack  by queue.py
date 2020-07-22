"""
Implement the given stack by using queue
explanation
First push all the list elemenents into stack,then print the top of the stack,then
use pop operation and again print the top with size of stack.

Input description
list of numbers

Output description
First line has top,second line has top after pop operation then print the size current
size op stack

Test Cases

Input
1 2 3 4 5
Output
5
4
4

Input
1 2 3 4 5 6 7 8 9 8 3
Output
3
8
10

Input
3 2 4 5 4 6 6 7 8 6
Output
6
8
9

Input
1
Output
1
1
-1

Input
1 2
Output
2
1
1

Solution:"""
from queue import Queue 

class Stack: 
	
	def __init__(self): 
		self.q1 = Queue() 
		self.q2 = Queue()  
		self.curr_size = 0

	def push(self, x): 
		self.curr_size += 1 
		self.q2.put(x)
		while (not self.q1.empty()): 
			self.q2.put(self.q1.queue[0]) 
			self.q1.get()
	
		self.q = self.q1 
		self.q1 = self.q2 
		self.q2 = self.q 

	def pop(self): 
		if (self.q1.empty()): 
			return
		self.q1.get() 
		self.curr_size -= 1

	def top(self): 
		if (self.q1.empty()): 
			return -1
		return self.q1.queue[0] 

	def size(self): 
		return self.curr_size 

s = Stack()
l=list(map(int,input().split()))
for i in l:
    s.push(i)
print(s.top())    
s.pop()
print(s.top()) 
print(s.size()) 
 
