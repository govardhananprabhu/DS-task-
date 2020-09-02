"""
Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list Merge sort.

In des
First line contains inmteger N, denotes the size of linked list.
Second line contains N space separated integers, denotes nodes of linked list.

Ot des
Print the sorted nodes

5
3 5 2 4 1

1 2 3 4 5

3
3 2 1

1 2 3

7
2 44 3 55 7 6 11

2 3 6 7 11 44 55

5
3 2 666 44 12

2 3 12 44 666

1
1

1


Exp
From sample:
After sorting the given
linked list, the resultant matrix
will be 1->2->3->4->5.

Hint
Let head be the first node of the linked list to be sorted and headRef be the pointer to head. Note that we need a reference to head in MergeSort() as the implementation changes next links to sort the linked lists (not data at the nodes), so head node has to be changed if the data at the original head is not the smallest value in the linked list.

H 7
T 2000

Accolite linked list
"""
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None
	def append(self, new_value):  
		new_node = Node(new_value)  
		if self.head is None: 
			self.head = new_node 
			return
		curr_node = self.head 
		while curr_node.next is not None: 
			curr_node = curr_node.next 
		curr_node.next = new_node 
		
	def sortedMerge(self, a, b): 
		result = None
		if a == None: 
			return b 
		if b == None: 
			return a 
		if a.data <= b.data: 
			result = a 
			result.next = self.sortedMerge(a.next, b) 
		else: 
			result = b 
			result.next = self.sortedMerge(a, b.next) 
		return result 
	
	def mergeSort(self, h): 
		if h == None or h.next == None: 
			return h
		middle = self.getMiddle(h) 
		nexttomiddle = middle.next
		middle.next = None 
		left = self.mergeSort(h) 
		right = self.mergeSort(nexttomiddle) 
		sortedlist = self.sortedMerge(left, right) 
		return sortedlist  
	def getMiddle(self, head): 
		if (head == None): 
			return head 

		slow = head 
		fast = head 

		while (fast.next != None and
			fast.next.next != None): 
			slow = slow.next
			fast = fast.next.next
			
		return slow 
def printList(head): 
	if head is None: 
		print(' ') 
		return
	curr_node = head 
	while curr_node: 
		print(curr_node.data, end = " ") 
		curr_node = curr_node.next
	print(' ')
li = LinkedList()
N=int(input())
l=list(map(int,input().split()))
for i in range(N):
    li.append(l[i]) 
li.head = li.mergeSort(li.head)
printList(li.head) 
