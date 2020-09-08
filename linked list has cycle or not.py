"""
Given a array with that create a linked list, check if the linked list has loop or not.
H 7
T 1000
Tag yahoo linked list

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers,denotes nodes of linked list.

Ot des
Print yes if loop found, else print no.
4
20 4 15 20

yes

4
20 4 15 10

no

3
1 2 3

no

5
1 2 3 4 5

no

5
1 2 2 3 4

yes

Exp
From sample:
the node 20 creates the loop.

Hint
Traverse the list one by one and keep putting the node addresses in a Hash Table. At any point, if NULL is reached then return false and if next of current node points to any of the previously stored nodes in Hash then return true.

"""
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
			print (temp.data, end =" ") 
			temp = temp.next


	def detectLoop(self): 
		s = []
		temp = self.head 
		while (temp):  
			if (temp.data in s): 
				return True
			s.append(temp.data) 
	
			temp = temp.next
		return False
N = int(input())
l=list(map(int,input().split()))
llist = LinkedList()
for i in range(N-1,-1,-1):
    llist.push(l[i])
if( llist.detectLoop()): 
	print ("yes") 
else : 
	print ("no")
