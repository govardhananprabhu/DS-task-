"""Question:
Your friend has two bags he wants to mix the numbers backwards present inside
the bags,he was busy ina an intern so,he ask's you to complete the task,the
mixture should be alternaative.If some bag has more numbers join it at the end.

Input description

First line contains first bag's numbers,and second line has second bag's numbers

Output description

print the mixed numbers has output

Test cases

Input
1 2 3 4 5
1 2 3

Output
5 3 4 2 3 1 2 1


Input
1 2 3
1 2 3 4 5

Output
3 5 2 4 1 3 2 1


Input
4 2 3
4 2 3

Output
3 3 2 2 4 4

Input
7 8 6 5
1 3 2 5

Output
5 5 6 2 8 3 7 1


Input
1 1 1 1 1 
2 2 2 2 2 

Output
1 2 1 2 1 2 1 2 1 2

Solution:"""
class LinkedList(object): 
	def __init__(self):  
		self.head = None

     
	class Node(object): 
		def __init__(self, d): 
			self.data = d 
			self.next = None

	def push(self, new_data): 
		new_node = self.Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def merge(self, q): 
		p_curr = self.head 
		q_curr = q.head 

	    
		while p_curr != None and q_curr != None: 
			p_next = p_curr.next
			q_next = q_curr.next

	    
			q_curr.next = p_next 
			p_curr.next = q_curr 

			
			p_curr = p_next 
			q_curr = q_next 
		q.head = q_curr 
	def printList(self): 
		temp = self.head 
		while temp != None: 
			ans.append(str(temp.data)), 
			temp = temp.next
	 


llist1 = LinkedList() 
llist2 = LinkedList()
l1=input().split()
l2=input().split()
ans=[]
for i in l1:
    llist1.push(i) 
for j in l2:
    llist2.push(j) 
llist1.merge(llist2)
    
llist1.printList() 
llist2.printList()
print(*ans)

 
