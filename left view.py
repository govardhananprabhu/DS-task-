"""
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.The tree created by level order method.

In des
First line contains integer N,denotes size of array.
Second line contains N space separated integers,denotes linked list node.

Ot des
Print the left view of binary tree.

5
1 2 3 4 5

1 2 4

8
1 3 2 4 5 7 6 9

1 3 4 9 

1
1

1

4
1 5 3 4

1 5 4 

3
1 2 3

1 2
Exp
Input : 
                 1
               /   \
              2     3
             / \     
            4   5                 
Output : 1 2 4

Hint
He left view contains all nodes that are first nodes in their levels. A simple solution is to do level order traversal and print the first node in every level.

"""
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def leftViewUtil(root, level, max_level): 
	if root is None: 
		return
	if (max_level[0] < level): 
		print(root.data,end=" ") 
		max_level[0] = level 
	leftViewUtil(root.left, level + 1, max_level) 
	leftViewUtil(root.right, level + 1, max_level) 
def leftView(root): 
	max_level = [0] 
	leftViewUtil(root, 1, max_level) 
def insertLevelOrder(arr, root, i, n):  
    if i < n: 
        temp = Node(arr[i])  
        root = temp    
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)  
 
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n) 
    return root 
n=int(input())
arr=list(map(int,input().split()))
root = None
root = insertLevelOrder(arr, root, 0, n)  
leftView(root) 
