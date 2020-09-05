"""
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Note: Tree created from array by level order.

H 8
T 1000
Tag Ola cabs,tree

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers,denotes nodes of tree.

Ot des
Print the top view of tree with space separated between each nodes.

7
1 2 3 4 5 6 7

4 2 1 3 7

3
1 2 3

2 1 3

7
10 20 30 40 60 90 100

40 20 10 30 100

16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

16 8 4 2 1 3 7 15

3
11 22 33

22 11 33 

From sample:
       1
    /     \
   2       3
  /  \    /   \
4    5  6      7

Top view will be: 4 2 1 3 7
Hint:
Print from leftmost node to rightmost node.
"""
class newNode: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None
		self.hd = 0
def topview(root) : 

	if(root == None) : 
		return
	q = [] 
	m = dict() 
	hd = 0
	root.hd = hd  
	q.append(root) 

	while(len(q)) : 
		root = q[0] 
		hd = root.hd  
		if hd not in m: 
			m[hd] = root.data 
		if(root.left) :		 
			root.left.hd = hd - 1
			q.append(root.left) 
		
		if(root.right):		 
			root.right.hd = hd + 1
			q.append(root.right) 
		
		q.pop(0) 
	for i in sorted (m): 
		print(m[i], end = " ") 
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = newNode(arr[i])  
        root = temp   
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)  
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root
n=int(input())
arr=list(map(int,input().split()))
root = None
root = insertLevelOrder(arr, root, 0, n)
topview(root)
