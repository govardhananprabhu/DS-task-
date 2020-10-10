"""
Given a  array of size N, from array create BST and also given a positive integer k, find the k’th largest element in the Binary Search Tree.

H 8
T 2000
Tag accolite array

7
20 8 22 4 12 10 14
3
14

7
20 8 22 4 12 10 14
4
12

7
20 8 22 4 12 10 14
6
8

5
21 2 123 4 3
2
21

3
1 3 2
3
1

Exp
From sample:
the 3rd largest element is 14

Hint
The idea is to do reverse inorder traversal of BST. Keep a count of nodes visited.


"""
class Node: 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None
def kthLargestUtil(root, k, c): 
	if root == None or c[0] >= k: 
		return
	kthLargestUtil(root.right, k, c) 
	c[0] += 1
	if c[0] == k: 
		print(root.key) 
		return
	kthLargestUtil(root.left, k, c)  
def kthLargest(root, k): 
	c = [0]  
	kthLargestUtil(root, k, c) 
def insert(node, key): 
	if node == None: 
		return Node(key) 
	if key < node.key: 
		node.left = insert(node.left, key) 
	elif key > node.key: 
		node.right = insert(node.right, key) 
	return node 

N=int(input())
l=list(map(int,input().split()))
k=int(input())
root = None
root = insert(root, l[0]) 
for i in range(1,N):
    insert(root, l[i])
kthLargest(root, k) 
