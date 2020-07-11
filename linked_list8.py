"""Question
Guhan has many brands of biscuits,he wants to find how many biscuits are in each
brand,he has work to do,so he appointed a worker to find,assume you are the worker
now.

Input description
First line has biscuits present in linked list

Output description
print the name of biscuit with its count in each line

Test cases

Input
Milk Milk Milk Butter Butter Salt
Output
Milk : 3
Butter : 2
Salt : 1

Input
Britania Tiger ParleG Britania Britania Britania Britania Tiger
Output
Britania : 5
Tiger : 2
ParleG : 1

Input
ParleG ParleG ParleG ParleG ParleG ParleG ParleG
Output
ParleG : 7

Hint:
Find the brands present in list,then find each brands count. 

Solution:"""

class Node:
	def __init__(self, data): 
		self.data = data 
		self.next = None 
class LinkedList: 
	def __init__(self): 
		self.head = None 
	def push(self, new_data):
		new_node = Node(new_data)  
		new_node.next = self.head 
		self.head = new_node 
	def search(self, x):
		current = self.head
		c=0
		while current != None: 
			if current.data == x: 
				c+=1
			
			current = current.next
		
		ans.append(c)
llist = LinkedList() 
l=input().split()
l=l[::-1]
for i in l:
    llist.push(i)
ans=[]
l2=[]
l=l[::-1]
for i in l:
    if i not in l2:
        l2.append(i)
for i in l2:
    llist.search(i)
for i in range(len(l2)):
    print(l2[i]+" :",ans[i])
