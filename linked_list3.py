"""Question
Two person has some coins they need to find the maximum sum by considering both their coins,
The result list may contain nodes from both input lists. When constructing the result list,
we may switch to the other input list only at the point of intersection (which mean the two
node with the same value in the lists).Use linked list.

Input description
First line and second line contains number of coins in list.

Output description
Print the maximum sum linked list

Test cases
Input
1 2 3 4 5
2 3 4 5 6
Output
1 2 3 4 5 6

Input
74 4 8 3 1 3
1 5 4 7 8 4
Output
74 4 8 3 1 3

Input
1 2 3 4 5 6 7
2 4 3 1 5 6 7
Output
1 2 3 4 3 1 5 6 7


solution:"""

class LinkedList(object): 
	def __init__(self):  
		self.head = None 
	class Node(object): 
		def __init__(self, d): 
			self.data = d 
			self.next = None 
	def finalMaxSumList(self, a, b): 
		result = None
		pre1 = a 
		curr1 = a 
		pre2 = b 
		curr2 = b 
		while curr1 != None or curr2 != None: 

			sum1 = 0
			sum2 = 0

			while curr1 != None and curr2 != None and curr1.data != curr2.data: 
				if curr1.data < curr2.data: 
					sum1 += curr1.data 
					curr1 = curr1.next
				else: 
					sum2 += curr2.data 
					curr2 = curr2.next
			 
			if curr1 == None: 
				while curr2 != None: 
					sum2 += curr2.data 
					curr2 = curr2.next
			if curr2 == None: 
				while curr1 != None: 
					sum1 += curr1.data 
					curr1 = curr1.next
		 
			if pre1 == a and pre2 == b: 
				result = pre1 if (sum1 > sum2) else pre2 
			else: 
 
				if sum1 > sum2: 
					pre2.next = pre1.next
				else: 
					pre1.next = pre2.next
	    
			pre1 = curr1 
			pre2 = curr2 
			if curr1 != None: 
				curr1 = curr1.next
			if curr2 != None: 
				curr2 = curr2.next

		while result != None: 
			ans.append(result.data) 
			result = result.next
		print(*ans)
	def push(self, new_data):
		new_node = self.Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 


llist1 = LinkedList() 
llist2 = LinkedList() 
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
L1=L1[::-1]
L2=L2[::-1]
for i in L1:
    llist1.push(i) 

for j in L2:
    llist2.push(j)
ans=[]


llist1.finalMaxSumList(llist1.head, llist2.head) 

