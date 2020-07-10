"""Question
Guhan want's to remove kth element t times in the linked list,note that the t+k
should not exceed length of linked list,if exceeds print not possibe,t times will be done in the modified
linked list.

Input description
First line has the numbers in linked list,second line has t and k two integers

Output description
Print the linked list after removing

Test cases

Input
1 2 3 4 5 6
3 2
Output
1 5 6

Input
1 2 3 4 5
5 1
Output
Not possible

Input
1 2 3 4 5 6 7
1 6
Output
1 2 3 4 5 7

Input
1 2 3 4 5 6 7
6 1
Output
7

Input
12 2
7 9
Output
Not possible

Hints:
From the given linked list remove the kth element for every tth time.

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
	def deleteNode(self, position):  
		if self.head == None: 
			return
		temp = self.head 
		if position == 0: 
			self.head = temp.next
			temp = None
			return
		for i in range(position -1 ): 
			temp = temp.next
			if temp is None: 
				break
		if temp is None: 
			return
		if temp.next is None: 
			return
 
		next = temp.next.next 
		temp.next = None

		temp.next = next
	def printList(self): 
		temp = self.head 
		while(temp): 
			ans.append(temp.data) 
			temp = temp.next
		print(*ans)

l=list(map(int,input().split()))
l=l[::-1]
t,k=map(int,input().split())
llist = LinkedList()
for i in l:
    llist.push(i)
if(t+k>len(l)):
    print("Not possible")
else:
    for i in range(t):
        llist.deleteNode(k-1) 
    ans=[]

    llist.printList()

