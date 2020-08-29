"""
Given a Cirular Linked List split it into two halves circular lists. If there are odd number of nodes in the given circular linked list then out of the resulting two halved lists, first list should have one node more than the second list. The resultant lists should also be circular lists and not linear lists.

In des
First line contain integer N,denotes size of linked list.
Second line contain N space separated integers,denotes circular linked list nodes.

Ot des
In first line print the first half.
In second line print the second half.

4
11 2 56 12

11 2
56 12
Exp
From sample
11 and 2 are the first half and 56,12 are the second half of given circular linked list.

H 7
T 2000

Hint
10 Store the mid and last pointers of the circular linked list using tortoise and hare algorithm.
2) Make the second half circular.
3) Make the first half circular.
4) Set head (or start) pointers of the two linked lists.
""" 
class Node: 
 
	def __init__(self, data): 
		self.data = data 
		self.next = None 
class CircularLinkedList: 
	def __init__(self): 
		self.head = None
	def push(self, data): 
		ptr1 = Node(data) 
		temp = self.head 
		
		ptr1.next = self.head  
		if self.head is not None: 
			while(temp.next != self.head): 
				temp = temp.next
			temp.next = ptr1 

		else: 
			ptr1.next = ptr1 

		self.head = ptr1 

	def printList(self): 
		temp = self.head 
		if self.head is not None: 
			while(True): 
				print(temp.data,end=" ") 
				temp = temp.next
				if (temp == self.head): 
					break
	def splitList(self, head1, head2): 
		slow_ptr = self.head 
		fast_ptr = self.head 
	
		if self.head is None: 
			return
		while(fast_ptr.next != self.head and
			fast_ptr.next.next != self.head ): 
			fast_ptr = fast_ptr.next.next
			slow_ptr = slow_ptr.next
		if fast_ptr.next.next == self.head: 
			fast_ptr = fast_ptr.next
		head1.head = self.head 
		if self.head.next != self.head: 
			head2.head = slow_ptr.next
		fast_ptr.next = slow_ptr.next
		slow_ptr.next = self.head 
 
 
N=int(input())
l=liat(map(int,input().split()))
for i in l:
    head.push(i) 
head = CircularLinkedList() 
head1 = CircularLinkedList()
head2 = CircularLinkedList()
head.splitList(head1 , head2) 

head1.printList() 

head2.printList() 
