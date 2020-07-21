"""Question
Mohan has work to do but he is not feeling well,so he ask's help from his brother,
assume now you are mohan's brother,the work is to swap the numbers in the linked
list by pairwise.

Input description
Linked list's numbers

Output description
print the pairwise swaped linked list

Test cases

Input
1 2 3 4 5
output
2 1 4 3 5

Input
1 2
output
2 1

Input
2 4 3 1 5 7 6 8 9 0 11
output
4 2 1 3 7 5 8 6 0 9 11

Input
1
output
1

Input
2 1 4 3 5
output
1 2 3 4 5

Hints:
First node will become second node and second becomes first,continue till length of
linked list


Solution:"""
class Node:  
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList:  
	def __init__(self): 
		self.head = None

	def pairwiseSwap(self): 
		temp = self.head 
		
		if temp is None: 
			return
		
		while(temp is not None and temp.next is not None): 
			temp.data, temp.next.data = temp.next.data, temp.data 
			temp = temp.next.next
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def printList(self): 
		temp = self.head 
		while(temp): 
			ans.append(temp.data) 
			temp = temp.next


llist = LinkedList()
ans=[]
l=list(map(int,input().split()))
for i in range(len(l)-1,-1,-1):
       llist.push(l[i])
llist.pairwiseSwap() 
llist.printList()
print(*ans)
