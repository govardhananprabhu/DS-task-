"""Question
Docter strange has done a magic he made some copy of numbers,you need need remove
extra's,print the remaining in sorted and find the number of extra's.

Input description
first line has numbers in linked list

Output descriptiopn
First print the linked list
second print the removed count

Input
1 2 3 4 5 5
Output
1 2 3 4 5
1

Input
5 3 6 7 7 4 4
Output
3 4 5 6 7
2

Input
66 66 66 12 12 1
Output
1 12 66
3


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
 
	def deleteNode(self, key): 
		temp = self.head 

		if (temp is not None): 
			if (temp.data == key): 
				self.head = temp.next
				temp = None
				return
 
		while(temp is not None): 
			if temp.data == key: 
				break
			prev = temp 
			temp = temp.next

		if(temp == None): 
			return

		prev.next = temp.next

		temp = None
 
	def printList(self): 
		temp = self.head 
		while(temp): 
			ans.append(temp.data) 
			temp = temp.next
		print(*ans)	 
	def removeDuplicates(self): 
		temp = self.head 
		if temp is None: 
			return
		while temp.next is not None: 
			if temp.data == temp.next.data: 
				new = temp.next.next
				temp.next = None
				temp.next = new 
			else: 
				temp = temp.next
		return self.head 

 
llist = LinkedList()
ans=[]
l=list(map(int,input().split()))
l.sort()
l=l[::-1]
k=len(l)
for i in l:
    llist.push(i) 
llist.removeDuplicates() 
llist.printList()
print(k-len(ans))

