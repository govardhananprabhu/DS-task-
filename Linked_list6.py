"""Question
Hulk want's to climb steps faster,he has the ability to jump one step,
so find the count of steps he taken to reach and print the steps he used.

Input description
first line has linked list with numbers

Output description
print the steps first and count next.

Test cases

Input
1 2 3 4 5 6 7
Output
1 3 5 7
3

Input
2 4 6 8 0
Output
2 6 0
2

Input
22 33 4 44 55 66 7 7
Output
22 4 55 7
4

Solution:"""

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

def deleteAlt(head): 
	if (head == None): 
		return
	prev = head 
	now = head.next

	while (prev != None and now != None): 
		
	 
		prev.next = now.next
		now = None 
		prev = prev.next
		if (prev != None): 
			now = prev.next 
def push(head_ref, new_data): 
	new_node = Node(new_data) 
	new_node.data = new_data 
	new_node.next = head_ref 
	head_ref = new_node 
	return head_ref 
def prList(node): 
	while (node != None): 
		ans.append(node.data) 
		node = node.next
	print(*ans)
head = None
l=list(map(int,input().split()))
l=l[::-1]
for i in l:
    head = push(head, i) 
ans=[] 
deleteAlt(head) 
prList(head) 
print(len(l)-len(ans))
