"""Question

Given a Singly Linked List, write a function to delete a given node. Your function
must follow following constraints:
1) It must accept a pointer to the start node as the first parameter and node to be
deleted as the second parameter i.e., a pointer to head node is not global.
2) It should not return a pointer to the head node.
3) It should not accept pointer to pointer to the head node.

You may assume that the Linked List never becomes empty.

Let the function name be deleteNode(). In a straightforward implementation, the function
needs to modify the head pointer when the node to be deleted is the first node. As discussed,
we can’t use any of those approaches here.If not possible print -1 and given list.

Input description:
First line has numbers in list and second line has key to  be deleted

Output description:
print the linkeed list after deletion

Test cases

Input
1 2 3 4 5
4
Output
1 2 3 5

Input
1 2 3 4 5
5
Output
1 2 3 4

Input
1 2 3 4 5
6
Output
-1
1 2 3 4 5

Input
1
1
Output
-1
1

Input
1 2 3 4 5
3
Output
1 2 4 5

Solution:"""
class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None 
class LinkedList: 

	def __init__(self): 
		self.head = None

	def deleteNode(self, data): 
		temp = self.head 
		prev = self.head 
		if temp.data == data: 
			if temp.next is None: 
				print(-1) 
			else: 
				temp.data = temp.next.data 
				temp.next = temp.next.next
			return
		while temp.next is not None and temp.data != data: 
			prev = temp 
			temp = temp.next
		if temp.next is None and temp.data !=data: 
			print(-1) 
		elif temp.next is None and temp.data == data: 
			prev.next = None
		else: 
			prev.next = temp.next	 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 
	def PrintList(self): 

		temp = self.head 
		while(temp): 
			ans.append(temp.data) 
			temp = temp.next
		print(*ans)
llist = LinkedList()
l=list(map(int,input().split()))
k=int(input())
ans=[]
for i in range(len(l)-1,-1,-1):
    llist.push(l[i]) 
llist.deleteNode(k) 
llist.PrintList()


 
