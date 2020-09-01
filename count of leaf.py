"""
Given a Binary Tree of size N , You have to count leaves in it. For example, there are two leaves in following tree.

In des
First line contain integer N,denotes size of tree.
Second line contains N space separated integers,denotes nodes of tree.

Ot des
print the count of leaves.

4
1 10 39 5

2

6
1 2 3 4 5 6
3

3
1 2 3
2

8
1 2 3 4 5 6 7 8
4

16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
8

Exp
From sample:
For example, there are two leaves in following tree 5,39.

        1
     /     \
   10      39
  /
 5


Hint
Traverse both sides of tree, and increase the count when there is no next node for left,right.

H 7
T 2000

""" 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None 
def getLeafCount(node): 
	if node is None: 
		return 0
	if(node.left is None and node.right is None): 
		return 1
	else: 
		return getLeafCount(node.left) + getLeafCount(node.right)
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
print(getLeafCount(root)) 
