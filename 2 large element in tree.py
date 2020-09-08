"""
Find the second largest element in BST created from given array.

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers, denotes nodes in tree

Ot des
Print the second largest element.

H 7
T 2000
Tag yahoo tree

7
50 20 30 40 70 60 80

70

2
10 5

5

4
10 20 30 5

20

4
1 2 3 4

3

6
11 22 3 44 5 78

44
Exp
From sample:
      50  
    /    \
   30     70  
   / \   / \  
  20 40 60 80
The 2nd largest element from tree is 70

Hint
The second largest element is second last element in inorder traversal and second element in reverse inorder traversal. We traverse given Binary Search Tree in reverse inorder and keep track of counts of nodes visited. Once the count becomes 2, we print the node.
"""
class Node: 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None 
def secondLargestUtil(root, c): 
	if root == None or c[0] >= 2: 
		return
	secondLargestUtil(root.right, c)  
	c[0] += 1
	if c[0] == 2: 
		print(root.key) 
		return
	secondLargestUtil(root.left, c) 
def secondLargest(root): 
	c = [0] 
	secondLargestUtil(root, c)  
def insert(node, key): 
	if node == None: 
		return Node(key)  
	if key < node.key: 
		node.left = insert(node.left, key) 
	elif key > node.key: 
		node.right = insert(node.right, key) 
	return node 

root = None
n=int(input())
l=list(map(int,input().split()))
for i in l:
    root = insert(root, i) 
secondLargest(root)  
