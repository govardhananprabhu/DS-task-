"""Ouestion
In auto stand there are N number of auto's,Only the first auto can go out first and
while returning it should parked at the last,and the second auto... till K auto's.
Note that it is possible any auto can go out any number of times according to K.
The auto's numbers are given in linked list.

Input description:
First line has two inputs N number of auto's and K auto's can move,second line has
n auto's in linked list.

Output description:
print the arrangedc linked list

Test cases:

Input
5 2
1 2 3 4 5
Output
3 4 5 1 2

Input
5 5
1 2 3 4 5
Output
1 2 3 4 5

Input
5 0
1 2 3 4 5
Output
1 2 3 4 5

Input
5 8
1 2 3 4 5
Output
4 5 1 2 3

Input
5 85
1 2 3 4 5
Output
1 2 3 4 5

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
	def printList(self): 
		temp = self.head 
		while(temp): 
			ans.append(temp.data), 
			temp = temp.next

	def rotate(self, k):
		if k == 0: 
			return

		current = self.head 
		
	 
		if current is None: 
			return 
		kthNode = current 
		while(current.next is not None): 
			current = current.next

		current.next = self.head 
		self.head = kthNode.next
		kthNode.next = None




llist = LinkedList()
N,K=map(int,input().split())
L=list(map(int,input().split()))
L=L[::-1]
for i in L:
    llist.push(i) 

for i in range(K):
    llist.rotate(1) 

ans=[]
llist.printList()
print(*ans)

