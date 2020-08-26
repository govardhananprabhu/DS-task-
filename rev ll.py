"""
Given a linked list of N nodes. The task is to reverse this list.

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.

Input:
LinkedList: 2->7->8->9->10
Output: 10 9 8 7 2
Explanation: After reversing the list,
elements are 10->9->8->7->2.
Hint
The task is to complete the function reverseList() with head reference as the only argument and should return new head after reversing the list.

H 6
T 1000


"""
class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None
	def reverse(self): 
		prev = None
		current = self.head 
		while(current is not None): 
			next = current.next
			current.next = prev 
			prev = current 
			current = next
		self.head = prev 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def printList(self): 
		temp = self.head 
		while(temp): 
			print(temp.data,end=" ") 
			temp = temp.next


n=int(input())
l=list(map(int,input().split()))
llist = LinkedList() 
for i in range(n-1,-1,-1):
    llist.push(l[i]) 

llist.reverse() 
llist.printList() 

