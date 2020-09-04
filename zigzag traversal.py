"""
Given a Binary Tree. Find the Zig-Zag Traversal of the Binary Tree.Tree created by level order.

H 7
T 2000

Tag cisco tree


In des
First line contain integer N,denotes size of array.
Second line contains N space separated integers, denotes nodes of linked list

Ot des
Print the zigzag traversed nodes

5
1 2 3 4 5

1 3 2 4 5

3
1 2 3
1 3 2

6
1 3 2 5 4 6
1 2 3 5 4 6

15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1 3 2 4 5 6 7 15 14 13 12 11 10 9 8

8
11 3 22 43 24 100 78 99
11 22 3 43 24 100 78 99 


Exp
From sample
           1
        /     \
       2       3
      / \
     4   5
the output of the created tree is 1 3 2 4 5 which is zig zagly traversed.

Hint
Traverse using level order but traverse alternativelt first right to left then left to right till last node.


""" 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None
def zizagtraversal(root): 
	if root is None: 
		return 
	currentLevel = [] 
	nextLevel = [] 
	ltr = True
	currentLevel.append(root) 
	while len(currentLevel) > 0: 
		temp = currentLevel.pop(-1) 
		print(temp.data, "", end="") 

		if ltr: 
			if temp.left: 
				nextLevel.append(temp.left) 
			if temp.right: 
				nextLevel.append(temp.right) 
		else: 
			if temp.right: 
				nextLevel.append(temp.right) 
			if temp.left: 
				nextLevel.append(temp.left) 

		if len(currentLevel) == 0: 
			ltr = not ltr 
			currentLevel, nextLevel = nextLevel, currentLevel 
n=int(input())
arr=list(map(int,input().split()))
def insertLevelOrder(arr, root, i, n):  
    if i < n: 
        temp = Node(arr[i])  
        root = temp   
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)  
 
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root 
root = None
root = insertLevelOrder(arr, root, 0, n) 
zizagtraversal(root) 
