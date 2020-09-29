"""
Given a Binary Search Tree (BST) and a range [min, max], remove all keys which are outside the given range. The modified tree should also be BST.

H 7 T 2000
Tag accolite tree

In des
First line contain integer N, denotes size of array.
Second line contains N space separated integers,denotes nodes of tree.
Third line contains 2 space separated integers,denotes the range.

Ot des
Print the modified BST in inorder traversal.

7
6 -13 14 -8 15 13 7
-10 13
-8 6 7 13


4
3 1 2 4
1 4
1 2 3 4

6
2 1 3 6 5 9
3 6
3 5 6

3
2 1 3
2 3
2 3

8
1 4 3 2 77 5 -1 3
3 77
3 3 4 5 77

Exp
From sample:
-8 6 7 13 are the values present inside the range
Hint
There are two possible cases for every node.
1) Node’s key is outside the given range. This case has two sub-cases.
a) Node’s key is smaller than the min value.
b) Node’s key is greater that the max value.
The idea is to fix the tree in Postorder fashion. When we visit a node, we make sure that its left and right sub-trees are already fixed. In case 1.a), we simply remove root and return right sub-tree as new root. In case 1.b), we remove root and return left sub-tree as new root.


"""
class newNode:  
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None

def removeOutsideRange(root, Min, Max): 
	if root == None: 
		return None
	root.left = removeOutsideRange(root.left, Min, Max) 
	root.right = removeOutsideRange(root.right, Min, Max) 

	if root.key < Min: 
		rChild = root.right 
		return rChild 
		
	if root.key > Max: 
		lChild = root.left 
		return lChild 
		
	return root 

def insert(root, key): 
	if root == None: 
		return newNode(key) 
	if root.key > key: 
		root.left = insert(root.left, key) 
	else: 
		root.right = insert(root.right, key) 
	return root  
def inorderTraversal(root): 
	if root: 
		inorderTraversal( root.left) 
		print(root.key, end = " ") 
		inorderTraversal( root.right) 

n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
root = None
for i in l:
    root = insert(root, i) 
root = removeOutsideRange(root, a, b) 
inorderTraversal(root) 

 
