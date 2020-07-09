""" Question
You have two purse,you need take pairs of coins which is equal to x,
find the count of pairs taken outside.Solve it by linked list.

Input description
Fist line and second line has coins in linked list,third line has
the value of x.

Output description
Print the count

Input
1 2 3 4 5
1 2 3 4 5
10
Output
1

Input
4 3 5 7 11 2 1
2 3 4 5 6 8 12
9
Output
5

Input
1 2
1
2
Output
1

Solution:"""
class Node: 
	def __init__(self,data): 
		self.data = data 
		self.next = None



def push(head_ref,new_data): 
	new_node=Node(new_data) 
	new_node.next = head_ref 
	head_ref = new_node 
	return head_ref 
 
def countPairs(head1, head2, x): 
	count = 0

	p1 = head1 
	while(p1 != None): 

		p2 = head2 
		while(p2 != None): 

			if ((p1.data + p2.data) == x): 
				count+=1
			p2 = p2.next
			
		p1 = p1.next	 
	return count 
 
head1 = None
head2 = None
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
x=int(input())
for i in L1:
    head1=push(head1, i) 
for j in L2:
    head2=push(head2, j) 
print(countPairs(head1, head2, x)) 
	
