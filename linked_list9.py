"""Question
A boy has many biscuits,he wants to find which type has more number of bisciut,
so he need not to buy that brand next time,if all the type has same count print
need to buy.

Input description
First line has biscuits in linked list

Output description
print the type with count

Test cases

Input
Milk Milk salt sweet butter salt salt
Output
salt : 3

Input
Milk parleG parleG Tiger Crack_Jack
Output
parleG : 2

Input
Milk parleG Tiger Crack_Jack
Output
Need to buy

Hint:
Find the brand which is present many times than others in linked list.

Solution :"""
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
	def search(self, x):
		current = self.head
		c=0
		while current != None: 
			if current.data == x: 
				c+=1
			
			current = current.next
		ans.append(c)
llist = LinkedList() 
l=input().split()
l=l[::-1]
for i in l:
    llist.push(i)
ans=[]
l2=[]
l=l[::-1]
for i in l:
    if i not in l2:
        l2.append(i)
for i in l2:
    llist.search(i)
k=max(ans)
if(len(ans)==ans.count(ans[0])):
    print("Need to buy")
else:
    print(l2[ans.index(k)]+" :",k)
