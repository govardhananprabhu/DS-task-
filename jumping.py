"""
Question
Given a positive number X. Find all Jumping Numbers smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it
differ by only 1. All single digit numbers are considered as Jumping Numbers.
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Input description
First line has integer denoting the range
Output description
print the number till the range 

Input
20
Output
0 1 2 3 4 5 6 7 8 9 10 12

Input
2
Output
0 1 2

Input
105
Output
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98 101

Hint
One Simple Solution is to traverse all numbers from 0 to x. For every traversed number, check if it is a Jumping number.
If yes, then print it. Otherwise ignore it. Time Complexity of this solution is O(x).
Solution:""" 

class Queue: 
	def __init__(self): 
		self.lst = [] 

	def is_empty(self): 
		return self.lst == [] 

	def enqueue(self, elem): 
		self.lst.append(elem) 

	def dequeue(self): 
		return self.lst.pop(0) 

def bfs(x, num): 
	q = Queue() 
	q.enqueue(num) 
	while (not q.is_empty()): 
		num = q.dequeue() 

		if num<= x: 
			ans.append(int(num)) 
			last_dig = num % 10 
			if last_dig == 0: 
				q.enqueue((num * 10) + (last_dig + 1))
			elif last_dig == 9: 
				q.enqueue((num * 10) + (last_dig - 1)) 
			else: 
				q.enqueue((num * 10) + (last_dig - 1)) 
				q.enqueue((num * 10) + (last_dig + 1))  
def printJumping(x): 
	ans.append(int(0)) 
	for i in range(1, 10): 
		bfs(x, i) 
ans=[]
x = int(input())
printJumping(x)
ans.sort()
print(*ans)
