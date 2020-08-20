"""
Given a Linked List and a number n, write a function that returns the value at the n’th node from the end of the Linked List.

In des
First line contain integer N,denotes size of linked list.
Second line contain N space separated integers,denotes nodes of linked list.

Ot des
Print the nth node from the end.

5
1 2 3 4 5
2

4

Exp
From sample
4 is the 2nd element from the end.

Hint
Calculate the length of Linked List. Let the length be len.
Print the (len – n + 1)th node from the beginning of the Linked List.

H 7
T 2000


"""
class Node: 
	def __init__(self, new_data): 
		self.data = new_data 
		self.next = None
	
class LinkedList: 
	def __init__(self): 
		self.head = None 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def printNthFromLast(self, n): 
		temp = self.head 
		
		length = 0
		while temp is not None: 
			temp = temp.next
			length += 1
		if n > length:
			print('-1') 
			return
		temp = self.head 
		for i in range(0, length - n): 
			temp = temp.next
		print(temp.data) 

N=int(input())
l=list(map(int,input().split()))
n=int(input())

llist = LinkedList() 
for i in range(N-1,-1,-1):
    llist.push(l[i]) 

llist.printNthFromLast(n) 
