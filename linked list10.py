"""Question
Ashok owns a bakery shop, he has types of biscuits,some of them are saled,so he
need to refill types which are saled.The type which has max count is not saled,
so the types which has the count less than max are saled. 

Input description
First line has biscuits in linked list

Output description
print the type with the current count and number of biscuit to add.

Test cases

Input
Milk Milk Salt Salt Sweet
Output
Milk : 2 Add : 0
Salt : 2 Add : 0
Sweet : 1 Add : 1

Input
Milk Salt Salt Sweet Chilly Chocalate Salt
Output
Milk : 1 Add : 2
Salt : 3 Add : 0
Sweet : 1 Add : 2
Chilly : 1 Add : 2
Chocalate : 1 Add : 2

Input
Tiger Tiger Tiger Tiger ParleG Marie
Output
Tiger : 4 Add : 0
ParleG : 1 Add : 3
Marie : 1 Add : 3

Hint:
Find the types of brand present,then find the max count,print each type with current
count and number of count to add with the current which equals to max.

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
for i in range(len(l2)):
    print(l2[i]+" :",ans[i],"Add :",k-ans[i])

